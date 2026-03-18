# Bugzilla Wrangler Report: Android Media
**Generated:** 2026-03-18

---

## Session Info

| Field | Value |
|-------|-------|
| **Date** | 2026-03-18 |
| **Scope profile** | `android` — Firefox for Android::Media + GeckoView::Media |
| **Seed timeframe** | 2025-12-18 → 2026-03-18 (90 days) |
| **Seed count** | **8 (low)** |
| **Seed mode** | mixed-seed (4 created + 4 changed = 8 unique) |
| **Cache** | Supplemented by prior-session cache (2026-03-17) — `reports/wrangler_cache_android.json` |

> **⚠️ Low Seed Count Warning**
> Only 8 bugs were returned from the primary seed queries for this session. The `android` scope profile is narrow (Firefox for Android::Media and GeckoView::Media), resulting in limited seed volume. Keyword expansion, targeted search, and the prior-session cache were used aggressively to compensate. Bugs from Core::Audio/Video that directly drive Fenix crashes (notably the EnsureTimeStretcher topcrash) were pulled in via dep-crawl scope expansion. Consider widening the profile to `Firefox for Android::General` in future runs.

---

## Seed Info

### Seed Bugs (by severity)

**S2**
- [2016829](https://bugzilla.mozilla.org/show_bug.cgi?id=2016829) — Android alarms going off stop Firefox from playing YouTube videos until app is force quit *(NEW, changed today)*

**S3**
- [2003004](https://bugzilla.mozilla.org/show_bug.cgi?id=2003004) — In portrait orientation, initial access of YouTube tabs forces display orientation into landscape *(NEW, 20 comments)*
- [2009725](https://bugzilla.mozilla.org/show_bug.cgi?id=2009725) — getUserMedia throws exception after stopping different camera stream tracks *(UNCONFIRMED)*
- [2003776](https://bugzilla.mozilla.org/show_bug.cgi?id=2003776) — Picture in picture problem *(NEW)*
- [1894494](https://bugzilla.mozilla.org/show_bug.cgi?id=1894494) — Playing list of audio files hang after while *(NEW, 20 comments)*

**S4**
- [2010746](https://bugzilla.mozilla.org/show_bug.cgi?id=2010746) — App always revert to landscape mode after exiting a full-screen video from YouTube *(NEW)*
- [2007946](https://bugzilla.mozilla.org/show_bug.cgi?id=2007946) — Closing tab forces app into landscape mode when next tab has YouTube open *(UNCONFIRMED)*
- [1996175](https://bugzilla.mozilla.org/show_bug.cgi?id=1996175) — Fullscreen security indicator hidden when third-party PiP player is active *(NEW)*

### Creation Date Timeline

```
Dec 2025    Jan 2026       Feb 2026     Mar 2026
-----------+---------------+------------+---------
  [x][x]   |  [x][x][x]   |    [x]     |
```

| Month | Count |
|-------|-------|
| Dec 2025 | 2 |
| Jan 2026 | 3 |
| Feb 2026 | 1 |
| Pre-Dec (Query B additions) | 2 |

---

## Theme 1: EnsureTimeStretcher Audio Decoder Crash (Topcrash)

**Rank: 1 | Signal: Very High (topcrash, >1,000 reports/30d, ASSIGNED)**

### User-Facing Impact

Firefox crashes during audio playback — specifically in the audio decoder's time-stretching path used for pitch-preserving speed adjustment. This is a Fenix **topcrash** and has been generating over 1,000 crash reports per month continuously. It is **actively being worked on** by Paul Adenot (:padenot).

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|--------|---------|----------|--------|--------------|---------------------|
| [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) | Crash in `mozilla::AudioDecoderInputTrack::EnsureTimeStretcher` `topcrash` | S2 | ASSIGNED — Paul Adenot (:padenot) | 2026-03-16 | [1,273 crashes](https://crashes.mozilla.org/signatures?q=signature%3A%22mozilla%3A%3AAudioDecoderInputTrack%3A%3AEnsureTimeStretcher%22) |

### Socorro Crash Data

Signature: [`mozilla::AudioDecoderInputTrack::EnsureTimeStretcher`](https://crashes.mozilla.org/signatures?q=signature%3A%22mozilla%3A%3AAudioDecoderInputTrack%3A%3AEnsureTimeStretcher%22)

| Window | Count | Trend |
|--------|-------|-------|
| 2026-01-17 → 2026-02-17 | 1,473 | — |
| 2026-02-17 → 2026-03-18 | 1,273 | ↓ Falling (-14%) |

- **Product:** Fenix (Firefox for Android)
- **Priority:** P2 | **In Core::Audio/Video**
- **Trend:** Falling but sustained above 1,000/month — still the #1 media crash in Fenix

### Timeline

- **2026-01-20:** [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) filed. Quickly triaged to S2 P2, assigned to Paul Adenot.
- **2026-03-16:** Last activity — investigation ongoing.

The falling trend suggests partial mitigation may be in flight. With P2 and an assignee, this has the best triage posture of any bug in this report.

---

## Theme 2: Media Notification Controls Broken / Stale

**Rank: 2 | Signal: High (S2 just resolved + active cluster)**

### User-Facing Impact

The Android system media notification (the persistent playback card in the notification shade that lets users control playback without opening Firefox) has multiple interrelated failure modes: controls don't respond, the wrong state is displayed, the notification doesn't dismiss, or it never appears. An S2 P2 instance was **resolved today (2026-03-18)** by John Lin (:jhlin), signaling recent active investment — but several older bugs remain open with no assignees.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2017451](https://bugzilla.mozilla.org/show_bug.cgi?id=2017451) | Music controls in the notification drawer fail to work | S2 | **RESOLVED** today by John Lin (:jhlin) | 2026-03-18 *(today)* |
| [1998726](https://bugzilla.mozilla.org/show_bug.cgi?id=1998726) | The player in the notification shade is broken when watching videos | S4 | UNCONFIRMED | 2025-12-09 |
| [1992980](https://bugzilla.mozilla.org/show_bug.cgi?id=1992980) | Notification badge remains on Realme devices after a website plays audio | S3 | NEW | 2025-11-13 |
| [1898072](https://bugzilla.mozilla.org/show_bug.cgi?id=1898072) | YouTube player notification doesn't disappear from phone when closing a video | S3 | NEW | 2024-10-14 |
| [1809285](https://bugzilla.mozilla.org/show_bug.cgi?id=1809285) | Missing system media notification | S3 | NEW | 2024-07-17 |
| [1795113](https://bugzilla.mozilla.org/show_bug.cgi?id=1795113) | The Play/Pause button does not remain displayed on the media notification | S3 | NEW | 2024-07-17 |

### Timeline

- **2022-10-13:** [1795113](https://bugzilla.mozilla.org/show_bug.cgi?id=1795113) filed — play/pause button missing. Still open 3.5 years later.
- **2023-01-09:** [1809285](https://bugzilla.mozilla.org/show_bug.cgi?id=1809285) filed — notification entirely absent. Still open.
- **2024-05-21:** [1898072](https://bugzilla.mozilla.org/show_bug.cgi?id=1898072) filed — stale notification ghost after closing video. 8 comments.
- **2025-10-07:** [1992980](https://bugzilla.mozilla.org/show_bug.cgi?id=1992980) filed — Realme-specific notification badge stuck. Triaged.
- **2026-02-17:** [2017451](https://bugzilla.mozilla.org/show_bug.cgi?id=2017451) filed — S2 P2 controls non-responsive. Immediately assigned. **RESOLVED 2026-03-18** (today).

The resolution of 2017451 today is a positive signal. However, the four older bugs (1795113, 1809285, 1898072, 1992980) represent a persistent and unresolved notification reliability problem spanning years.

> **⚠️ Stagnation:** [1795113](https://bugzilla.mozilla.org/show_bug.cgi?id=1795113) and [1809285](https://bugzilla.mozilla.org/show_bug.cgi?id=1809285) are S3 bugs with no activity since July 2024 — both over 18 months without resolution.

---

## Theme 3: Video and Audio Playback Disrupted by System Events

**Rank: 3 | Signal: High**

### User-Facing Impact

Users encounter video or audio playback breaking mid-session — not from user action, but from external system events: a phone alarm fires, an audio output device changes, or the app is briefly backgrounded. Recovery requires force-quitting and relaunching Firefox. The lead bug (S2) was changed **today**.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2016829](https://bugzilla.mozilla.org/show_bug.cgi?id=2016829) | Android alarms going off stop Firefox from playing YouTube videos until app is force quit | S2 | NEW | 2026-03-18 *(today)* |
| [1962813](https://bugzilla.mozilla.org/show_bug.cgi?id=1962813) | Certain website content for video or cloud game streaming services does not play content (GeckoView) | S2 | UNCONFIRMED | 2025-11-27 |
| [1894494](https://bugzilla.mozilla.org/show_bug.cgi?id=1894494) | Playing list of audio files hang after while | S3 | NEW | 2026-02-03 |
| [1887748](https://bugzilla.mozilla.org/show_bug.cgi?id=1887748) | Audio output switch causes video playback to break (GeckoView) | S3 | NEW | 2024-04-03 |

### Timeline

- **2024-03-25:** [1887748](https://bugzilla.mozilla.org/show_bug.cgi?id=1887748) filed — audio output switch breaks playback. Unassigned, stale.
- **2024-05-01:** [1894494](https://bugzilla.mozilla.org/show_bug.cgi?id=1894494) filed — audio playlist hang. Two years open, 20 comments. Active as recently as Feb 2026.
- **2025-04-25:** [1962813](https://bugzilla.mozilla.org/show_bug.cgi?id=1962813) filed (GeckoView) — video/cloud game streaming broken. S2 UNCONFIRMED.
- **2026-02-13:** [2016829](https://bugzilla.mozilla.org/show_bug.cgi?id=2016829) filed — alarm-triggered playback failure. 13 comments, changed today. Unassigned.

> **⚠️ Stagnation:** [1887748](https://bugzilla.mozilla.org/show_bug.cgi?id=1887748) is S3 with no activity since April 2024 (nearly 2 years).

---

## Theme 4: Fullscreen Video Rendering Regressions

**Rank: 4 | Signal: High (but deeply stagnant)**

### User-Facing Impact

Fullscreen video playback shows persistent visual glitches across multiple device types — white bars/margins, cropped or overflowing video, controls not registering taps. Many bugs carry the `regression` keyword. Xiaomi/MIUI devices appear disproportionately. Despite an **S2 regression open since 2023**, none of these bugs have an active Mozilla assignee.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1844573](https://bugzilla.mozilla.org/show_bug.cgi?id=1844573) | White margin when entering fullscreen mode on most pages `regression` | S2 | NEW | 2024-07-09 |
| [1904654](https://bugzilla.mozilla.org/show_bug.cgi?id=1904654) | Fullscreen video has white bars on Xiaomi Mi 9 (notch display) `regression` | S3 | NEW | 2025-07-03 |
| [1750416](https://bugzilla.mozilla.org/show_bug.cgi?id=1750416) | Fullscreen video cropped/incorrect size when ContentDelegate is set (GeckoView) `regression` P3 | S3 | NEW | 2025-02-11 |
| [1956795](https://bugzilla.mozilla.org/show_bug.cgi?id=1956795) | Fullscreen in splitscreen mode goes over notification bar | S3 | NEW | 2025-04-21 |
| [1813870](https://bugzilla.mozilla.org/show_bug.cgi?id=1813870) | Tapping in fullscreen videos doesn't register properly P2 | S3 | NEW | 2025-03-10 |
| [1879782](https://bugzilla.mozilla.org/show_bug.cgi?id=1879782) | Controls missing in video player in fullscreen portrait mode `regression` `regressionwindow-wanted` | S3 | NEW | 2024-05-27 |
| [1870658](https://bugzilla.mozilla.org/show_bug.cgi?id=1870658) | Fullscreen video problem on Xiaomi Redmi Note 11S (MIUI 13) | S3 | NEW | 2024-06-27 |

### Timeline

- **2022-01-16:** [1750416](https://bugzilla.mozilla.org/show_bug.cgi?id=1750416) filed — GeckoView fullscreen cropping regression. Open for 4 years with P3.
- **2023-01-30:** [1813870](https://bugzilla.mozilla.org/show_bug.cgi?id=1813870) — touch targets broken in fullscreen. P2 but unowned.
- **2023-07-20:** [1844573](https://bugzilla.mozilla.org/show_bug.cgi?id=1844573) — **S2 regression**, white margin in fullscreen. No activity since July 2024.
- **2024-02-11:** [1879782](https://bugzilla.mozilla.org/show_bug.cgi?id=1879782) — controls gone in portrait fullscreen; `regressionwindow-wanted` set but never resolved.
- **2024-06-25:** [1904654](https://bugzilla.mozilla.org/show_bug.cgi?id=1904654) — 28 comments (highest in dataset), Xiaomi notch white bars. Last active July 2025.

> **⚠️ Stagnation — multiple critical entries:**
> - [1844573](https://bugzilla.mozilla.org/show_bug.cgi?id=1844573): **S2 regression**, no activity since July 2024 (8+ months).
> - [1904654](https://bugzilla.mozilla.org/show_bug.cgi?id=1904654): **S3 regression**, 28 comments, no activity since July 2025.
> - [1879782](https://bugzilla.mozilla.org/show_bug.cgi?id=1879782): **S3 regression** with `regressionwindow-wanted` unresolved since May 2024.
> - [1750416](https://bugzilla.mozilla.org/show_bug.cgi?id=1750416): **S3 regression**, P3, no activity since Feb 2025.

---

## Theme 5: YouTube/Video Tab Landscape Orientation Hijacking

**Rank: 5 | Signal: High (active engagement)**

### User-Facing Impact

When a YouTube tab is open or a video enters fullscreen, Firefox forces the phone into landscape orientation even when the user has not requested it and even when their device has rotation locked. The inverse also occurs: Firefox forces portrait for vertical videos even when the user has locked their screen to landscape. Three of four bugs are from the last 4 months, making this an actively growing issue cluster.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2003004](https://bugzilla.mozilla.org/show_bug.cgi?id=2003004) | In portrait orientation, initial access of YouTube tabs forces display into landscape | S3 | NEW | 2026-03-09 |
| [2010746](https://bugzilla.mozilla.org/show_bug.cgi?id=2010746) | App always reverts to landscape mode after exiting a full-screen video from YouTube | S4 | NEW | 2026-02-23 |
| [2007946](https://bugzilla.mozilla.org/show_bug.cgi?id=2007946) | Closing tab forces app into landscape mode when next tab has YouTube open | S4 | UNCONFIRMED | 2026-01-13 |
| [1973415](https://bugzilla.mozilla.org/show_bug.cgi?id=1973415) | Firefox always auto-rotates to portrait when fullscreening a vertical video, ignoring device rotation lock | S3 | NEW | 2025-07-21 |

### Timeline

- **2025-06-22:** [1973415](https://bugzilla.mozilla.org/show_bug.cgi?id=1973415) filed — vertical video ignores lock. Stagnant since July 2025.
- **2025-11-28:** [2003004](https://bugzilla.mozilla.org/show_bug.cgi?id=2003004) filed — most engaged bug in this theme, 20 comments, active as recently as 9 March 2026.
- **2025-12-29:** [2007946](https://bugzilla.mozilla.org/show_bug.cgi?id=2007946) filed — tab-close triggers landscape lock.
- **2026-01-16:** [2010746](https://bugzilla.mozilla.org/show_bug.cgi?id=2010746) filed — can't return to portrait after fullscreen YouTube.

No meta-bug. All unassigned. The core root cause across all four is likely a single YouTube-specific orientation handling path that Firefox is not overriding or resetting correctly.

---

## Theme 6: Picture-in-Picture (PiP) Functionality Issues

**Rank: 6 | Signal: Medium**

### User-Facing Impact

Firefox for Android's PiP feature has multiple independent failure modes: gestures for opening PiP don't work on Samsung OneUI devices, control buttons (play/pause, settings) are absent or show unexpected mic/camera icons, and a security indicator is incorrectly hidden while PiP is active. Two bugs were changed in March 2026, indicating active user engagement.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2003776](https://bugzilla.mozilla.org/show_bug.cgi?id=2003776) | Picture in picture problem | S3 | NEW | 2026-03-02 |
| [2007658](https://bugzilla.mozilla.org/show_bug.cgi?id=2007658) | In PiP, rewind/fast-forward not working; mic and camera icons appear instead | -- | NEW | 2026-03-09 |
| [1996175](https://bugzilla.mozilla.org/show_bug.cgi?id=1996175) | Fullscreen security indicator hidden when third-party PiP player is active | S4 | NEW | 2025-12-24 |
| [1957199](https://bugzilla.mozilla.org/show_bug.cgi?id=1957199) | PiP doesn't work with swipe gestures (OneUI + 3rd party launcher) | S3 | NEW | 2025-04-15 |
| [1912252](https://bugzilla.mozilla.org/show_bug.cgi?id=1912252) | PiP doesn't display pause/play and settings options, only fullscreen and close | S3 | NEW | 2025-04-25 |

### Timeline

- **2024-08-08:** [1912252](https://bugzilla.mozilla.org/show_bug.cgi?id=1912252) filed — missing controls. Open since then, no activity in 11 months.
- **2025-03-29:** [1957199](https://bugzilla.mozilla.org/show_bug.cgi?id=1957199) filed — swipe failure on Samsung. 4 comments, stagnant since April 2025.
- **2025-10-24:** [1996175](https://bugzilla.mozilla.org/show_bug.cgi?id=1996175) filed — security indicator hidden. 12 comments, `reporter-external` keyword (filed by external security researcher or reporter).
- **2025-12-24:** [2007658](https://bugzilla.mozilla.org/show_bug.cgi?id=2007658) filed — wrong icons in PiP controls. Changed 2026-03-09.

The security dimension of [1996175](https://bugzilla.mozilla.org/show_bug.cgi?id=1996175) warrants a closer look: hiding the fullscreen security indicator could allow phishing in PiP contexts.

---

## Theme 7: Camera Capture and getUserMedia Failures

**Rank: 7 | Signal: Medium (crash-enriched, declining)**

### User-Facing Impact

Web camera capture via `getUserMedia` breaks when stream tracks are stopped and restarted. A related crash in the WebRTC `CameraSession` has been generating reports over the past three months, though volume is declining as old Fenix 141.x builds age out.

### Breadcrumbs

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|--------|---------|----------|--------|--------------|---------------------|
| [2009725](https://bugzilla.mozilla.org/show_bug.cgi?id=2009725) | getUserMedia throws exception after stopping different camera stream tracks (GeckoView) | S3 | UNCONFIRMED | 2026-02-18 | — |
| [1979932](https://bugzilla.mozilla.org/show_bug.cgi?id=1979932) | Crash: `org.webrtc.CameraSession$-CC.onShutdown` | S3 | NEW | 2025-12-04 | [67](https://crashes.mozilla.org/signatures?q=signature%3A%22java.lang.RuntimeException%3A%20at%20org.webrtc.CameraSession%24-CC.onShutdown%28CameraSession.java%29%22) |
| [1967052](https://bugzilla.mozilla.org/show_bug.cgi?id=1967052) | WebRTC camera capture breaks when another browser simultaneously uses the same device (GeckoView) | S3 | UNCONFIRMED | 2025-07-21 | — |
| [1972416](https://bugzilla.mozilla.org/show_bug.cgi?id=1972416) | Camera and Microphone permission not displayed on Android 16 | S3 | NEW | 2025-06-16 | — |

### Socorro Crash Data: CameraSession

| Window | Count | Trend |
|--------|-------|-------|
| 2025-12-18 → 2026-01-17 | 139 | — |
| 2026-01-17 → 2026-02-17 | 193 | ↑ Peak |
| 2026-02-17 → 2026-03-18 | 67 | ↓ Falling |

Affected builds are Fenix 141.x (significantly behind current 147–148), suggesting the crash is self-resolving as users update. The Android 16 permission gap ([1972416](https://bugzilla.mozilla.org/show_bug.cgi?id=1972416)) is worth tracking as Android 16 approaches general availability.

---

## Emerging Issue: Wrong Audio Permission on File Input (Regression)

**Below theme threshold (1 bug) — highlighted as emerging signal**

[2002689](https://bugzilla.mozilla.org/show_bug.cgi?id=2002689) — *Firefox for Android requests "Music and Audio" permission when the user taps an `input type="file"` for image files* — **S3, NEW, `regression`, 13 comments**, last changed 2025-12-09. No assignee.

A behavioral regression causing Firefox to request Android media storage permissions in an irrelevant context (image picker). Thirteen comments with engaged reporters indicate broad reach. The `regression` keyword confirms a known-good state was broken by a specific change. Identifying the regressing commit (via `regressionwindow-wanted` or `mach bisect`) would be a low-effort, high-value follow-up.

---

## Closing

### Ranked Signal Summary

| Rank | Theme | Breadcrumbs | Meta-bug | Top Severity | Assignee | Notes |
|------|-------|-------------|----------|--------------|----------|-------|
| 1 | EnsureTimeStretcher Audio Crash | 1 + Socorro | None | S2 | padenot@mozilla.com | 1,273 crashes/30d; topcrash; falling trend |
| 2 | Media Notification Controls | 6 | None | S2 | jhlin (RESOLVED 2017451) | S2 fixed today; 4 older bugs stagnant |
| 3 | Video/Audio Playback Disrupted by System Events | 4 | None | S2 | Nobody | S2 active today; GeckoView S2 unconfirmed |
| 4 | Fullscreen Rendering Regressions | 7 | None | S2 | Nobody | Multiple regressions; deeply stagnant |
| 5 | YouTube Landscape Orientation Hijacking | 4 | None | S3 | Nobody | Active engagement Mar 2026 |
| 6 | PiP Functionality Issues | 5 | None | S3 | Nobody | Possible security dimension in 1996175 |
| 7 | Camera Capture & getUserMedia | 4 | None | S3 | Nobody | CameraSession crash declining |

**Cross-cutting observation:** With the exception of Theme 1 and the just-resolved Theme 2 lead bug, **every bug in this report is unassigned**. The Android Media component shows a pattern of bugs accumulating without ownership, particularly in fullscreen rendering (Theme 4), where S2 and S3 regressions have remained open for 1–4 years.

---

### Resources Used

| Resource | Usage |
|----------|-------|
| Bugzilla REST API | 14 fetches (2 seed, 8 keyword expansion, 4 targeted lookups) |
| Prior-session cache | Supplemented seed with 2 additional high-signal bugs (2017451, 2011539) |
| Socorro `socorro-cli` | 8 queries (Fenix facet, CameraSession ×3, ForegroundService ×2, EnsureTimeStretcher ×2) |
| cc_count | Not returned by API; comment_count used as proxy |
| Dep crawl | 0 deps (all seed bugs had empty depends_on/blocks) |

**Note:** `cc_count` was not returned by the Bugzilla API even when requested in `include_fields`. Signal scoring relied on `comment_count` as the community engagement proxy. Per-bug UI fetches would resolve this.

---

### Suggestions for Improving This Skill

1. **Broaden the android scope profile** — Add `Firefox for Android::General` to substantially increase seed volume without losing focus. Consider also sweeping `Core::Audio/Video` for Fenix-affecting crashes.
2. **Cache cross-session with age check** — The prior-session cache (written yesterday) contained two critical bugs (2017451, 2011539) that were missed in the fresh seed. A configurable staleness threshold (e.g., "use cache if < 24 hours old") would prevent this gap.
3. **cc_count fallback** — The field is systematically absent from batch REST API calls. Add a per-bug fallback for the top 5 signal bugs.
4. **Socorro signature discovery** — The `--facet signature` + grep approach worked well here. Consider adding it as a default step for the android scope rather than relying on crash-keyworded seed bugs.

---

> *"Not all those who wander are lost — but all those who have `regressionwindow-wanted` set and no activity for 18 months probably are."*