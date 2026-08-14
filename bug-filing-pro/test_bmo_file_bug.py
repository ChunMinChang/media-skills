import contextlib
import importlib.machinery
import importlib.util
import io
from pathlib import Path
import unittest
import urllib.parse


def load_module():
    loader = importlib.machinery.SourceFileLoader(
        "bmo_file_bug", str(Path(__file__).with_name("bmo-file-bug"))
    )
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


bmo_file_bug = load_module()


class ResolveGroupNamesTest(unittest.TestCase):
    def test_preserves_internal_names_without_api_lookup(self):
        def unexpected_api(*args, **kwargs):
            self.fail("internal names must not trigger an API lookup")

        self.assertEqual(
            bmo_file_bug.resolve_group_names(
                ["media-core-security"], group_api=unexpected_api
            ),
            ["media-core-security"],
        )

    def test_resolves_visible_label(self):
        calls = []

        def group_api(*args, **kwargs):
            calls.append((args, kwargs))
            return {
                "groups": [
                    {
                        "name": "media-core-security",
                        "description": "Security-Sensitive Media Bug",
                    }
                ]
            }

        self.assertEqual(
            bmo_file_bug.resolve_group_names(
                ["Security-Sensitive Media Bug"], group_api=group_api
            ),
            ["media-core-security"],
        )
        self.assertEqual(calls, [(("GET", "group"), {"on_error": "raise"})])

    def test_resolves_visible_label_case_insensitively(self):
        def group_api(*args, **kwargs):
            return {
                "groups": [
                    {
                        "name": "media-core-security",
                        "description": "Security-Sensitive Media Bug",
                    }
                ]
            }

        self.assertEqual(
            bmo_file_bug.resolve_group_names(
                ["security-sensitive media bug"], group_api=group_api
            ),
            ["media-core-security"],
        )

    def test_rejects_unknown_visible_label(self):
        def group_api(*args, **kwargs):
            return {"groups": []}

        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(
            SystemExit
        ) as raised:
            bmo_file_bug.resolve_group_names(
                ["Missing Security Group"], group_api=group_api
            )
        self.assertEqual(raised.exception.code, 2)
        self.assertIn(
            "unknown or unavailable Bugzilla group label", stderr.getvalue()
        )

    def test_browser_form_reports_omitted_groups(self):
        skipped = bmo_file_bug._skipped_for_form(
            {"groups": ["Security-Sensitive Media Bug"]}, []
        )
        self.assertEqual(skipped, ["groups: Security-Sensitive Media Bug"])


class WhiteboardTest(unittest.TestCase):
    def test_create_payload_includes_whiteboard(self):
        args = bmo_file_bug.build_parser().parse_args([
            "create",
            "--product", "Core",
            "--component", "Audio/Video",
            "--summary", "Test bug",
            "--description", "Test description",
            "--whiteboard", "[Keep hidden]",
        ])

        payload = bmo_file_bug.build_bug_payload(args)

        self.assertEqual(payload["whiteboard"], "[Keep hidden]")

    def test_flags_dry_run_includes_whiteboard(self):
        args = bmo_file_bug.build_parser().parse_args([
            "flags", "123",
            "--whiteboard", "[Keep hidden]",
            "--dry-run",
            "--preview", "none",
        ])
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            args.func(args)

        self.assertIn('"whiteboard": "[Keep hidden]"', stdout.getvalue())

    def test_browser_form_includes_whiteboard(self):
        url = bmo_file_bug._enter_bug_url({
            "product": "Core",
            "component": "Audio/Video",
            "summary": "Test bug",
            "whiteboard": "[Keep hidden]",
        })

        query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)

        self.assertEqual(query["status_whiteboard"], ["[Keep hidden]"])

    def test_rejects_duplicate_whiteboard_settings(self):
        args = bmo_file_bug.build_parser().parse_args([
            "create",
            "--product", "Core",
            "--component", "Audio/Video",
            "--summary", "Test bug",
            "--description", "Test description",
            "--whiteboard", "one",
            "--field", "whiteboard=two",
        ])

        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                bmo_file_bug.build_bug_payload(args)

        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
