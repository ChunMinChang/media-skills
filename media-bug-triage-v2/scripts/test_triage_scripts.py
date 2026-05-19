#!/usr/bin/env python3
"""Tests for the Firefox bug triage skill helper scripts.

Run from the repo root:

    python3 -m unittest discover -s mozilla/firefox/dot.claude/skills/triage/scripts

Stdlib only; mirrors the style of claude/test_session_sync.py.
"""

import io
import json
import os
import sys
import tempfile
import unittest
from unittest import mock

# Import the modules under test. Skill scripts are siblings; the shared
# bmo_client lives under ../../shared/ in the media-skills repo layout.
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "shared"),
)
import bmo_client
import apply_pending
import pending_store
import render_report
import scope_profiles
import triage_paths


# ---------------------------------------------------------------------------
# scope_profiles
# ---------------------------------------------------------------------------


class TestScopeProfiles(unittest.TestCase):

    def test_media_inference(self):
        self.assertEqual(
            scope_profiles.infer_profile("Core", "Audio/Video: Playback"), "media"
        )
        self.assertEqual(scope_profiles.infer_profile("Core", "Web Audio"), "media")

    def test_web_conferencing_inference(self):
        self.assertEqual(
            scope_profiles.infer_profile("Core", "WebRTC: Networking"),
            "web-conferencing",
        )
        self.assertEqual(
            scope_profiles.infer_profile("Core", "DOM: Screen Capture"),
            "web-conferencing",
        )

    def test_graphics_inference(self):
        self.assertEqual(
            scope_profiles.infer_profile("Core", "Graphics: WebRender"),
            "graphics",
        )
        self.assertEqual(
            scope_profiles.infer_profile("Core", "Web Painting"),
            "graphics",
        )

    def test_android_inference(self):
        self.assertEqual(
            scope_profiles.infer_profile("Firefox for Android", "Media"),
            "android",
        )
        self.assertEqual(
            scope_profiles.infer_profile("GeckoView", "Media"),
            "android",
        )
        # Android wins regardless of component.
        self.assertEqual(
            scope_profiles.infer_profile("GeckoView", "General"),
            "android",
        )

    def test_default_with_warning(self):
        buf = io.StringIO()
        with mock.patch("sys.stderr", buf):
            result = scope_profiles.infer_profile("Toolkit", "Storage")
        self.assertEqual(result, "media")
        self.assertIn("no profile match", buf.getvalue())

    def test_resolve_profile_known(self):
        self.assertEqual(scope_profiles.resolve_profile("Graphics"), "graphics")
        self.assertEqual(scope_profiles.resolve_profile(" media "), "media")
        self.assertIsNone(scope_profiles.resolve_profile(None))

    def test_resolve_profile_unknown(self):
        with self.assertRaises(ValueError) as ctx:
            scope_profiles.resolve_profile("not-a-profile")
        msg = str(ctx.exception)
        # Error message must list the valid options.
        for key in scope_profiles.PROFILES:
            self.assertIn(key, msg)

    def test_components_and_product(self):
        comps = scope_profiles.components_for("media")
        self.assertIn("Audio/Video", comps)
        # Returned list is a copy — mutation must not bleed into the table.
        comps.append("FAKE")
        self.assertNotIn("FAKE", scope_profiles.components_for("media"))
        self.assertEqual(scope_profiles.product_for("media"), "Core")
        self.assertEqual(
            scope_profiles.product_for("android"),
            ["Firefox for Android", "GeckoView"],
        )


# ---------------------------------------------------------------------------
# pending_store
# ---------------------------------------------------------------------------


class TestPendingStore(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.mkdtemp(prefix="triage-test-")
        triage_paths.set_override(self._tmp)

    def tearDown(self):
        triage_paths.clear_override()
        import shutil

        shutil.rmtree(self._tmp, ignore_errors=True)

    # -- paths

    def test_paths_respect_override(self):
        self.assertEqual(pending_store.state_dir(), self._tmp)
        self.assertEqual(
            pending_store.pending_path(123),
            os.path.join(self._tmp, "bug-123", "pending.json"),
        )
        self.assertEqual(
            pending_store.bug_snapshot_path(123),
            os.path.join(self._tmp, "bug-123", "bug.json"),
        )
        self.assertEqual(
            pending_store.log_path(),
            os.path.join(self._tmp, "triage-log.json"),
        )

    # -- save / load round-trip

    def test_save_and_load_round_trip(self):
        payload = {
            "schema_version": 1,
            "bug_id": 42,
            "created_at": "2026-05-14T10:00:00Z",
            "branch": "1a",
            "comment": "hello",
        }
        path = pending_store.save_pending(payload)
        self.assertTrue(os.path.exists(path))
        loaded = pending_store.load_pending(42)
        self.assertEqual(loaded, payload)

    def test_save_requires_bug_id_and_created_at(self):
        with self.assertRaises(ValueError):
            pending_store.save_pending({"created_at": "x"})
        with self.assertRaises(ValueError):
            pending_store.save_pending({"bug_id": 1})

    def test_load_missing_returns_none(self):
        self.assertIsNone(pending_store.load_pending(9999))

    def test_delete_pending_idempotent(self):
        payload = {"bug_id": 7, "created_at": "2026-05-14T10:00:00Z"}
        pending_store.save_pending(payload)
        self.assertTrue(pending_store.delete_pending(7))
        self.assertFalse(pending_store.delete_pending(7))

    # -- atomicity

    def test_save_is_atomic(self):
        payload = {"bug_id": 1, "created_at": "2026-05-14T10:00:00Z"}
        pending_store.save_pending(payload)
        # No leftover .tmp in the per-bug folder after a successful write.
        bug_dir = os.path.dirname(pending_store.pending_path(1))
        leftovers = [f for f in os.listdir(bug_dir) if f.endswith(".tmp")]
        self.assertEqual(leftovers, [])

    # -- stale detection

    def test_is_stale_true_when_bug_newer(self):
        payload = {"bug_id": 1, "created_at": "2026-05-14T10:00:00Z"}
        self.assertTrue(pending_store.is_stale(payload, "2026-05-14T10:00:01Z"))

    def test_is_stale_false_when_bug_older_or_equal(self):
        payload = {"bug_id": 1, "created_at": "2026-05-14T10:00:00Z"}
        self.assertFalse(pending_store.is_stale(payload, "2026-05-14T10:00:00Z"))
        self.assertFalse(pending_store.is_stale(payload, "2026-05-13T10:00:00Z"))

    def test_is_stale_handles_missing_inputs(self):
        self.assertFalse(pending_store.is_stale(None, "anything"))
        self.assertFalse(pending_store.is_stale({"bug_id": 1}, "x"))
        self.assertFalse(
            pending_store.is_stale(
                {"bug_id": 1, "created_at": "2026-05-14T10:00:00Z"}, ""
            )
        )

    # -- log append

    def test_append_log_creates_array(self):
        pending_store.append_log_entry({"bug_id": 1, "decision": "skipped"})
        pending_store.append_log_entry({"bug_id": 2, "decision": "triaged"})
        with open(pending_store.log_path(), "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["bug_id"], 1)
        self.assertEqual(data[1]["decision"], "triaged")

    def test_append_log_survives_corrupt_existing_file(self):
        os.makedirs(pending_store.state_dir(), exist_ok=True)
        with open(pending_store.log_path(), "w", encoding="utf-8") as f:
            f.write("not-json garbage")
        pending_store.append_log_entry({"bug_id": 3, "decision": "ok"})
        with open(pending_store.log_path(), "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data, [{"bug_id": 3, "decision": "ok"}])

    def test_now_iso_utc_shape(self):
        ts = pending_store.now_iso_utc()
        self.assertRegex(ts, r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


# ---------------------------------------------------------------------------
# apply_pending
# ---------------------------------------------------------------------------


def _make_bug(bug_id=1, last_change_time="2026-05-14T10:00:00Z", **extra):
    bug = {
        "id": bug_id,
        "summary": "test bug",
        "status": "NEW",
        "product": "Core",
        "component": "Audio/Video: Playback",
        "creation_time": "2026-05-14T09:00:00Z",
        "last_change_time": last_change_time,
        "severity": "--",
        "priority": "--",
        "keywords": [],
        "flags": [],
        "comments": [],
    }
    bug.update(extra)
    return bug


def _make_pending(bug_id=1, branch="1b", **extra):
    payload = {
        "schema_version": 1,
        "bug_id": bug_id,
        "title": "test",
        "branch": branch,
        "scope": "media",
        "created_at": "2026-05-14T09:30:00Z",
        "comment": "Reproduced. Setting P2/S3.",
        "priority": "P2",
        "severity": "S3",
    }
    payload.update(extra)
    return payload


def _make_api_responder(bug, write_response=None, fail_on=None):
    """Build a side_effect for bmo_client.api that fakes a GET and writes.

    ``bug`` is the dict returned for the ``GET bug/{id}`` call.
    ``write_response`` is what every successful write call returns ({}).
    ``fail_on`` is a callable (method, path) -> bool; matching writes raise
    SystemExit(1), simulating bmo_client's HTTP-error path.
    """
    write_response = write_response if write_response is not None else {}

    def responder(method, path, data=None):
        if method == "GET" and path.startswith("bug/"):
            return {"bugs": [bug]}
        if fail_on is not None and fail_on(method, path):
            raise SystemExit(1)
        return write_response

    return responder


class _ApplyTestCase(unittest.TestCase):
    """Shared scaffolding for apply_pending tests."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp(prefix="triage-apply-")
        triage_paths.set_override(self._tmp)
        # ensure_auth() always passes by default; individual tests can
        # override with side_effect=SystemExit to simulate a missing key.
        self._auth_patcher = mock.patch.object(bmo_client, "ensure_auth")
        self._auth_patcher.start()

    def tearDown(self):
        self._auth_patcher.stop()
        triage_paths.clear_override()
        import shutil

        shutil.rmtree(self._tmp, ignore_errors=True)


class TestApplyPendingExitCodes(_ApplyTestCase):

    def test_missing_pending_file_exits_2(self):
        with mock.patch.object(bmo_client, "api") as api:
            code = apply_pending.run(9999, dry_run=True, assume_yes=True)
        self.assertEqual(code, 2)
        api.assert_not_called()

    def test_stale_draft_exits_6(self):
        pending_store.save_pending(_make_pending(bug_id=1))
        bug = _make_bug(bug_id=1, last_change_time="2026-05-14T10:00:00Z")
        with mock.patch.object(
            bmo_client, "api", side_effect=_make_api_responder(bug)
        ):
            code = apply_pending.run(1, dry_run=True, assume_yes=True)
        self.assertEqual(code, 6)
        # Pending file preserved.
        self.assertIsNotNone(pending_store.load_pending(1))

    def test_missing_api_key_exits_3(self):
        pending_store.save_pending(_make_pending(bug_id=2))
        # Override the always-passing ensure_auth from setUp; bmo_client
        # signals a missing key via sys.exit(1).
        self._auth_patcher.stop()
        try:
            with mock.patch.object(
                bmo_client, "ensure_auth", side_effect=SystemExit(1)
            ), mock.patch.object(bmo_client, "api") as api:
                code = apply_pending.run(2, dry_run=False, assume_yes=True)
            self.assertEqual(code, 3)
            self.assertIsNotNone(pending_store.load_pending(2))
            # No HTTP work should have happened.
            api.assert_not_called()
        finally:
            self._auth_patcher.start()

    def test_dry_run_succeeds_without_writes(self):
        pending_store.save_pending(_make_pending(bug_id=3))
        bug = _make_bug(bug_id=3, last_change_time="2026-05-14T09:00:00Z")
        calls = []

        def responder(method, path, data=None):
            calls.append((method, path))
            if method == "GET":
                return {"bugs": [bug]}
            return {}

        with mock.patch.object(bmo_client, "api", side_effect=responder):
            code = apply_pending.run(3, dry_run=True, assume_yes=True)
        self.assertEqual(code, 0)
        # Only the GET fetch ran; no PUT/POST.
        methods = [m for m, _ in calls]
        self.assertEqual(methods, ["GET"])
        # Dry run does not delete the pending file.
        self.assertIsNotNone(pending_store.load_pending(3))

    def test_full_success_deletes_pending_and_logs(self):
        pending = _make_pending(bug_id=4, ni_targets=["a@example.com"])
        pending_store.save_pending(pending)
        bug = _make_bug(bug_id=4, last_change_time="2026-05-14T09:00:00Z")
        calls = []

        def responder(method, path, data=None):
            calls.append((method, path))
            if method == "GET":
                return {"bugs": [bug]}
            return {}

        with mock.patch.object(bmo_client, "api", side_effect=responder):
            code = apply_pending.run(4, dry_run=False, assume_yes=True)
        self.assertEqual(code, 0)
        self.assertIsNone(pending_store.load_pending(4))
        with open(pending_store.log_path(), "r", encoding="utf-8") as f:
            log = json.load(f)
        self.assertEqual(len(log), 1)
        self.assertEqual(log[0]["bug_id"], 4)
        self.assertEqual(log[0]["decision"], "triaged")
        # Expected call sequence: GET, set_fields PUT, comment POST, needinfo PUT.
        methods = [m for m, _ in calls]
        self.assertEqual(methods, ["GET", "PUT", "POST", "PUT"])

    def test_partial_failure_preserves_pending(self):
        pending_store.save_pending(_make_pending(bug_id=5))
        bug = _make_bug(bug_id=5, last_change_time="2026-05-14T09:00:00Z")
        responder = _make_api_responder(
            bug,
            fail_on=lambda method, path: method == "POST" and "comment" in path,
        )
        with mock.patch.object(bmo_client, "api", side_effect=responder):
            code = apply_pending.run(5, dry_run=False, assume_yes=True)
        self.assertEqual(code, 4)
        # Pending preserved for retry; log entry records partial.
        self.assertIsNotNone(pending_store.load_pending(5))
        with open(pending_store.log_path(), "r", encoding="utf-8") as f:
            log = json.load(f)
        self.assertEqual(log[0]["decision"], "apply_partial")
        self.assertIn("post_comment", log[0]["failed"])

    def test_user_abort_exits_5(self):
        pending_store.save_pending(_make_pending(bug_id=6))
        bug = _make_bug(bug_id=6, last_change_time="2026-05-14T09:00:00Z")
        # Empty input on stdin means abort.
        stdin = io.StringIO("\n")
        calls = []

        def responder(method, path, data=None):
            calls.append((method, path))
            if method == "GET":
                return {"bugs": [bug]}
            return {}

        with mock.patch.object(bmo_client, "api", side_effect=responder):
            code = apply_pending.run(6, dry_run=False, assume_yes=False, stdin=stdin)
        self.assertEqual(code, 5)
        # Only the GET fetch ran; no writes after abort.
        methods = [m for m, _ in calls]
        self.assertEqual(methods, ["GET"])
        # Pending preserved.
        self.assertIsNotNone(pending_store.load_pending(6))


class TestApplyPendingFieldReconciliation(unittest.TestCase):

    def test_skip_already_set_scalar(self):
        pending = _make_pending(priority="P2", severity="S3")
        current = _make_bug(priority="P2", severity="S4")
        fields = apply_pending.build_field_payload(pending, current)
        # priority already P2 → skipped; severity differs → included.
        self.assertNotIn("priority", fields)
        self.assertEqual(fields["severity"], "S3")

    def test_compute_missing_blocks(self):
        pending = _make_pending(blocks_add=[1, 2, 3])
        current = _make_bug(blocks=[2])
        fields = apply_pending.build_field_payload(pending, current)
        self.assertEqual(fields["blocks"], {"add": [1, 3]})

    def test_no_changes_returns_empty(self):
        pending = _make_pending(priority="P2", severity="S3")
        current = _make_bug(priority="P2", severity="S3")
        fields = apply_pending.build_field_payload(pending, current)
        self.assertEqual(fields, {})


# ---------------------------------------------------------------------------
# render_report
# ---------------------------------------------------------------------------


class TestRenderReport(unittest.TestCase):

    def test_header_contains_bug_id_and_url(self):
        bug = _make_bug(bug_id=42, summary="Foo")
        body = render_report.render(bug, _make_pending(bug_id=42), "media", {}, [])
        self.assertIn("Bug 42 Triage Analysis", body)
        self.assertIn("https://bugzilla.mozilla.org/show_bug.cgi?id=42", body)

    def test_includes_scope_and_assessment(self):
        bug = _make_bug(bug_id=7, severity="S3", priority="P3")
        pending = _make_pending(bug_id=7, severity="S2", priority="P2")
        body = render_report.render(bug, pending, "graphics", {}, [])
        self.assertIn("Scope:** graphics", body)
        self.assertIn("Suggested Severity:** S2", body)
        self.assertIn("Suggested Priority:** P2", body)

    def test_classification_table_present(self):
        bug = _make_bug(bug_id=8)
        body = render_report.render(bug, {}, "media", {}, [])
        self.assertIn("## Classification", body)
        for label in ("Clear STR", "Test Case", "Crash Stack", "Fuzzing"):
            self.assertIn(label, body)

    def test_draft_response_block(self):
        pending = _make_pending(comment="Hello there.")
        body = render_report.render(_make_bug(), pending, "media", {}, [])
        self.assertIn("## Draft Response", body)
        self.assertIn("Hello there.", body)

    def test_usage_footer_when_provided(self):
        body = render_report.render(
            _make_bug(bug_id=1),
            {},
            "media",
            {"bugs_fetched": 12, "searches_issued": 3, "inaccessible": 1},
            [],
        )
        self.assertIn("Bugs fetched: 12", body)
        self.assertIn("Inaccessible bugs (permissions / deleted): 1", body)

    def test_regression_section_only_when_signal_present(self):
        body_plain = render_report.render(
            _make_bug(bug_id=1),
            {},
            "media",
            {},
            [],
        )
        self.assertNotIn("Regression Timeline", body_plain)
        body_reg = render_report.render(
            _make_bug(bug_id=1, regressed_by=[111, 222]),
            {},
            "media",
            {},
            [],
        )
        self.assertIn("Regression Timeline", body_reg)
        # regressed_by IDs must be linkable, not bare.
        self.assertIn("[111](https://bugzilla.mozilla.org/show_bug.cgi?id=111)",
                      body_reg)
        self.assertIn("[222](https://bugzilla.mozilla.org/show_bug.cgi?id=222)",
                      body_reg)

    def test_header_uses_linkable_bug_ref(self):
        body = render_report.render(
            _make_bug(bug_id=99), _make_pending(bug_id=99), "media", {}, []
        )
        self.assertIn(
            "**Bug:** [99](https://bugzilla.mozilla.org/show_bug.cgi?id=99)",
            body,
        )

    def test_crash_signature_links_to_socorro(self):
        bug = _make_bug(bug_id=5, cf_crash_signature="[@ FooBar::Baz(int)]")
        body = render_report.render(bug, {}, "media", {}, [])
        self.assertIn("Crash signatures:", body)
        self.assertIn(
            "(https://crash-stats.mozilla.org/signatures/?signature=", body
        )

    def test_security_bug_flagged_in_info(self):
        bug = _make_bug(
            bug_id=7, groups=["core-security"], summary="redact me"
        )
        body = render_report.render(bug, {}, "media", {}, [])
        self.assertIn("**Security:** restricted", body)
        # Summary still appears in the triage bug's own info section — the
        # rule is about *referencing* security bugs from elsewhere.
        self.assertIn("redact me", body)

    def test_sec_prefix_groups_count_as_restricted(self):
        bug = _make_bug(bug_id=8, groups=[{"name": "sec-high"}])
        body = render_report.render(bug, {}, "media", {}, [])
        self.assertIn("**Security:** restricted", body)

    def test_codebase_findings_link_to_searchfox(self):
        findings = [{"path": "dom/media/MediaDecoder.cpp", "note": "see Foo()"}]
        body = render_report.render(_make_bug(bug_id=1), {}, "media", {}, findings)
        self.assertIn("Codebase Investigation", body)
        self.assertIn(
            "[dom/media/MediaDecoder.cpp]"
            "(https://searchfox.org/mozilla-central/source/"
            "dom/media/MediaDecoder.cpp)",
            body,
        )

    def test_dupe_and_blocks_use_linkable_refs(self):
        pending = _make_pending(bug_id=1, dupe_of=99, blocks_add=[111, 222])
        body = render_report.render(_make_bug(bug_id=1), pending, "media", {}, [])
        self.assertIn(
            "Resolve DUPLICATE of [99](https://bugzilla.mozilla.org/show_bug.cgi?id=99)",
            body,
        )
        self.assertIn(
            "[111](https://bugzilla.mozilla.org/show_bug.cgi?id=111)", body
        )


class TestRenderReportCli(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.mkdtemp(prefix="render-cli-")

    def tearDown(self):
        import shutil

        shutil.rmtree(self._tmp, ignore_errors=True)

    def _write(self, name, payload):
        path = os.path.join(self._tmp, name)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f)
        return path

    def test_cli_writes_default_path(self):
        bug_path = self._write("bug.json", _make_bug(bug_id=33))
        pending_path = self._write("pending.json", _make_pending(bug_id=33))
        out_path = os.path.join(self._tmp, "out.md")
        code = render_report.main(
            [
                "--bug",
                bug_path,
                "--pending",
                pending_path,
                "--scope",
                "media",
                "--out",
                out_path,
            ]
        )
        self.assertEqual(code, 0)
        with open(out_path, "r", encoding="utf-8") as f:
            body = f.read()
        self.assertIn("Bug 33 Triage Analysis", body)

    def test_cli_invalid_input_exits_1(self):
        # Missing --bug/--pending and missing --out
        code = render_report.main([])
        self.assertEqual(code, 1)


# ---------------------------------------------------------------------------
# triage_paths
# ---------------------------------------------------------------------------


class TestTriagePathsResolution(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.mkdtemp(prefix="triage-paths-")
        self._cfg = os.path.join(self._tmp, "config.toml")
        self._cfg_patcher = mock.patch.object(triage_paths, "CONFIG_PATH", self._cfg)
        self._cfg_patcher.start()
        triage_paths.clear_override()

    def tearDown(self):
        self._cfg_patcher.stop()
        triage_paths.clear_override()
        import shutil

        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_unset_raises(self):
        with self.assertRaises(triage_paths.OutputRootUnset):
            triage_paths.output_root()

    def test_override_wins_over_config(self):
        triage_paths.persist_output_dir("/from-config")
        triage_paths.set_override("/from-override")
        self.assertEqual(triage_paths.output_root(), "/from-override")

    def test_config_when_no_override(self):
        triage_paths.persist_output_dir(self._tmp)
        self.assertEqual(triage_paths.output_root(), self._tmp)

    def test_per_bug_paths(self):
        triage_paths.set_override("/root")
        self.assertEqual(triage_paths.bug_dir(42), "/root/bug-42")
        self.assertEqual(triage_paths.report_path(42), "/root/bug-42/triage.md")
        self.assertEqual(triage_paths.pending_path(42), "/root/bug-42/pending.json")
        self.assertEqual(triage_paths.test_page_path(42), "/root/bug-42/test.html")
        self.assertEqual(triage_paths.bug_snapshot_path(42), "/root/bug-42/bug.json")
        self.assertEqual(triage_paths.log_path(), "/root/triage-log.json")

    def test_bug_id_coerced_from_string(self):
        triage_paths.set_override("/root")
        self.assertEqual(triage_paths.bug_dir("99"), "/root/bug-99")
        self.assertEqual(triage_paths.pending_path("99"), "/root/bug-99/pending.json")

    def test_persist_writes_and_reads_back(self):
        triage_paths.persist_output_dir(self._tmp)
        with open(self._cfg, "r", encoding="utf-8") as f:
            text = f.read()
        self.assertIn("output_dir", text)
        self.assertIn(self._tmp, text)
        self.assertEqual(triage_paths.read_output_dir_from_config(), self._tmp)

    def test_persist_replaces_existing_value(self):
        triage_paths.persist_output_dir("/first")
        triage_paths.persist_output_dir("/second")
        self.assertEqual(triage_paths.read_output_dir_from_config(), "/second")
        # No duplicate line in the file.
        with open(self._cfg, "r", encoding="utf-8") as f:
            occurrences = sum(1 for line in f if line.strip().startswith("output_dir"))
        self.assertEqual(occurrences, 1)

    def test_persist_preserves_other_fields(self):
        with open(self._cfg, "w", encoding="utf-8") as f:
            f.write('unrelated_field = "keep-me"\n')
            f.write('default_scope = "media"\n')
        triage_paths.persist_output_dir("/root")
        with open(self._cfg, "r", encoding="utf-8") as f:
            text = f.read()
        self.assertIn('unrelated_field = "keep-me"', text)
        self.assertIn('default_scope = "media"', text)
        self.assertIn('output_dir = "/root"', text)

    def test_toml_ignores_comments_and_whitespace(self):
        with open(self._cfg, "w", encoding="utf-8") as f:
            f.write("# header comment\n")
            f.write("\n")
            f.write('output_dir = "/path/from/toml"  # trailing\n')
            f.write('default_scope = "graphics"\n')
        self.assertEqual(triage_paths.read_output_dir_from_config(), "/path/from/toml")
        self.assertEqual(triage_paths.read_default_scope_from_config(), "graphics")


class TestTriagePathsCli(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.mkdtemp(prefix="triage-cli-")
        self._cfg = os.path.join(self._tmp, "config.toml")
        self._cfg_patcher = mock.patch.object(triage_paths, "CONFIG_PATH", self._cfg)
        self._cfg_patcher.start()

    def tearDown(self):
        self._cfg_patcher.stop()
        import shutil

        shutil.rmtree(self._tmp, ignore_errors=True)

    def _capture(self, argv):
        buf = io.StringIO()
        with mock.patch("sys.stdout", buf):
            code = triage_paths._cli(argv)
        return code, buf.getvalue().strip()

    def test_get_output_dir_empty_when_unset(self):
        code, out = self._capture(["--get-output-dir"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "")

    def test_set_then_get_round_trips(self):
        code, out = self._capture(["--set-output-dir", "/wonderland"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "/wonderland")
        code, out = self._capture(["--get-output-dir"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "/wonderland")

    def test_config_path_action(self):
        code, out = self._capture(["--config-path"])
        self.assertEqual(code, 0)
        self.assertEqual(out, self._cfg)


# ---------------------------------------------------------------------------
# Snapshot-based stale check
# ---------------------------------------------------------------------------


class TestSnapshotStaleCheck(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.mkdtemp(prefix="triage-snap-")
        triage_paths.set_override(self._tmp)

    def tearDown(self):
        triage_paths.clear_override()
        import shutil

        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_no_snapshot_returns_false(self):
        self.assertFalse(
            pending_store.is_stale_against_snapshot(1, "2026-05-14T10:00:00Z")
        )

    def test_snapshot_older_than_fresh_is_stale(self):
        pending_store.save_bug_snapshot(
            1, {"id": 1, "last_change_time": "2026-05-14T09:00:00Z"}
        )
        self.assertTrue(
            pending_store.is_stale_against_snapshot(1, "2026-05-14T10:00:00Z")
        )

    def test_snapshot_equal_or_newer_not_stale(self):
        pending_store.save_bug_snapshot(
            2, {"id": 2, "last_change_time": "2026-05-14T10:00:00Z"}
        )
        self.assertFalse(
            pending_store.is_stale_against_snapshot(2, "2026-05-14T10:00:00Z")
        )
        self.assertFalse(
            pending_store.is_stale_against_snapshot(2, "2026-05-14T09:00:00Z")
        )

    def test_snapshot_round_trip(self):
        bug = {"id": 5, "summary": "x", "last_change_time": "2026-05-14T10:00:00Z"}
        pending_store.save_bug_snapshot(5, bug)
        loaded = pending_store.load_bug_snapshot(5)
        self.assertEqual(loaded, bug)


if __name__ == "__main__":
    unittest.main()
