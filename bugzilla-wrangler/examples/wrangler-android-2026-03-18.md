# Firefox for Android Media Bug Wrangler Report

---

## Session Info

| Field | Value |
|-------|-------|
| **Report Generated** | 2026-03-18 |
| **Scope Profile** | `android` — Firefox for Android::Media + GeckoView::Media |
| **Seed Timeframe** | 2025-10-01 through 2026-03-15 |
| **Seed Count** | 24 unique bugs |
| **Seed Mode** | mixed-seed (15 created + 9 changed = 24 unique) |
| **Cache Freshness** | Live fetch (user-specified date range; new session) |
| **cc_count** | Not returned by Bugzilla REST API for these queries; comment_count used as engagement proxy |

---

## Seed Info

### Seed Bug List (priority-ordered)

**P2 / S2:**
- [1841246](https://bugzilla.mozilla.org/show_bug.cgi?id=1841246) — Prompts for EME/DRM from iframe popup show toplevel origin instead of frame origin (S2, P2, 34 comments)
- [2016829](https://bugzilla.mozilla.org/show_bug.cgi?id=2016829) — Android alarms stop Firefox from playing YouTube videos until app is force quit (S2, 13 comments)
- [1962813](https://bugzilla.mozilla.org/show_bug.cgi?id=1962813) — Certain website content for video or cloud game streaming services does not play (GeckoView, S2, 8 comments)

**S3 — within seed date window (created Oct 2025–Mar 2026):**
- [2003004](https://bugzilla.mozilla.org/show_bug.cgi?id=2003004) — Portrait orientation forces display to landscape when accessing YouTube tabs (S3, 20 comments)
- [2003776](https://bugzilla.mozilla.org/show_bug.cgi?id=2003776) — Picture in picture problem (S3, 11 comments)
- [2009725](https://bugzilla.mozilla.org/show_bug.cgi?id=2009725) — getUserMedia throws exception after stopping different camera stream tracks (GeckoView, S3, 6 comments)
- [2002689](https://bugzilla.mozilla.org/show_bug.cgi?id=2002689) — Firefox requests "Music and Audio" permission when tapping `input[type=file]` with image types (S3, regression, 13 comments)
- [1997634](https://bugzilla.mozilla.org/show_bug.cgi?id=1997634) — Build fails with JDK 21 due to deprecated source/target in ExoPlayer module (S3, 5 comments)
- [1997876](https://bugzilla.mozilla.org/show_bug.cgi?id=1997876) — Media Session API: Relative seek bug (GeckoView, S3, 2 comments)
- [2003860](https://bugzilla.mozilla.org/show_bug.cgi?id=2003860) — Huge amount of `media_state.*` events in `mozdata.fenix.events_stream` (S3, 1 comment)
- [2002874](https://bugzilla.mozilla.org/show_bug.cgi?id=2002874) — Missing context menu options when opening a PWA (S3, 7 comments)
- [1992980](https://bugzilla.mozilla.org/show_bug.cgi?id=1992980) — Notification badge persists on Realme devices after website plays audio (S3, triaged, 13 comments)
- [1993468](https://bugzilla.mozilla.org/show_bug.cgi?id=1993468) — Fullscreen "Subtitles/CC turned on" notification obscures subtitles for extended period (S3, 5 comments)

**S4 — within seed date window:**
- [2010746](https://bugzilla.mozilla.org/show_bug.cgi?id=2010746) — App always reverts to landscape after exiting fullscreen YouTube video (S4, 6 comments)
- [2007946](https://bugzilla.mozilla.org/show_bug.cgi?id=2007946) — Closing tab forces landscape mode when next tab has YouTube open (S4, 7 comments)
- [1996175](https://bugzilla.mozilla.org/show_bug.cgi?id=1996175) — Fullscreen security indicator hidden when third-party PiP player is active (S4, 12 comments)
- [1998726](https://bugzilla.mozilla.org/show_bug.cgi?id=1998726) — Player in notification shade broken when watching videos (S4, 5 comments)

**From Query B (recently changed, older bugs):**
- [1894494](https://bugzilla.mozilla.org/show_bug.cgi?id=1894494) — Playing a list of audio files hangs after a while (S3, 20 comments; last changed Feb 2026)
- [1870999](https://bugzilla.mozilla.org/show_bug.cgi?id=1870999) — YouTube thumbnails overlap when watching videos in landscape mode (S3, P3)
- [1979932](https://bugzilla.mozilla.org/show_bug.cgi?id=1979932) — Crash in `org.webrtc.CameraSession` (S3, crash, 6 comments)
- [1979738](https://bugzilla.mozilla.org/show_bug.cgi?id=1979738) — Glitches while swiping through Google images (S3, 8 comments)
- [1975861](https://bugzilla.mozilla.org/show_bug.cgi?id=1975861) — Video in website keeps playing even after closing Firefox (S3, 5 comments)
- [1890695](https://bugzilla.mozilla.org/show_bug.cgi?id=1890695) — Fullscreen video overflows screen in desktop mode (GeckoView, S3, 2 comments)
- [1984118](https://bugzilla.mozilla.org/show_bug.cgi?id=1984118) — Crash in `MediaNotification.kt` (`PendingIntent` NPE) (S4, crash, 4 comments)
- [1841246](https://bugzilla.mozilla.org/show_bug.cgi?id=1841246) — EME/DRM iframe popup (already listed above)
- [1962813](https://bugzilla.mozilla.org/show_bug.cgi?id=1962813) — Cloud gaming streaming (already listed above)

### Creation Date Distribution

```
Oct 2025: ████  (4 bugs)  1992980, 1993468, 1996175, [1841246 last changed here]
Nov 2025: █████ (5 bugs)  2002689, 2002874, 2003004, 2003776, 2003860
Dec 2025: ███   (3 bugs)  2007946, 1997634, 1997876
Jan 2026: ██    (2 bugs)  2009725, 2010746
Feb 2026: █     (1 bug)   2016829
Mar 2026:       (0 bugs)  [none created yet in window]
+ older bugs recently changed: 9 bugs from pre-Oct 2025
```

The seed is fairly representative across the window, with a cluster in November 2025. The 9 recently-changed older bugs show there is meaningful long-lived, unresolved backlog also being touched in this period.

---

## Theme 1: Fullscreen Video & Screen Orientation Dysfunction

### User-Facing Impact

Users frequently encounter videos or fullscreen content forcing the device into an incorrect screen orientation (usually unwanted landscape when in portrait, or stuck in landscape after exiting fullscreen). Separate sub-issues include visual rendering artifacts (white bars, cropped video, overflowing content) when entering fullscreen. Collectively these make watching video in Firefox for Android a friction-heavy experience compared to other browsers.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2003004](https://bugzilla.mozilla.org/show_bug.cgi?id=2003004) | Portrait orientation forces landscape when accessing YouTube tabs | S3 | NEW | 2026-03-09 |
| [2010746](https://bugzilla.mozilla.org/show_bug.cgi?id=2010746) | App always reverts to landscape after exiting fullscreen YouTube video | S4 | NEW | 2026-02-23 |
| [2007946](https://bugzilla.mozilla.org/show_bug.cgi?id=2007946) | Closing tab forces landscape mode when next tab has YouTube open | S4 | UNCONFIRMED | 2026-01-13 |
| [1992382](https://bugzilla.mozilla.org/show_bug.cgi?id=1992382) | [Firefox Android] fullscreen videos' screen orientation is locked | N/A | UNCONFIRMED | 2025-11-05 |
| [1973415](https://bugzilla.mozilla.org/show_bug.cgi?id=1973415) | Auto-rotates to portrait when fullscreening vertical video, even with rotation locked | S3 | NEW | 2025-07-21 |
| [1904654](https://bugzilla.mozilla.org/show_bug.cgi?id=1904654) | Fullscreen video has white bars on Xiaomi notch display | S3 (regression) | NEW | 2025-07-03 |
| [1996175](https://bugzilla.mozilla.org/show_bug.cgi?id=1996175) | Fullscreen security indicator hidden when third-party PiP player is active | S4 | NEW | 2025-12-24 |
| [1993468](https://bugzilla.mozilla.org/show_bug.cgi?id=1993468) | Fullscreen "CC turned on" notification obscures subtitles | S3 | NEW | 2025-11-07 |
| [1890695](https://bugzilla.mozilla.org/show_bug.cgi?id=1890695) | Fullscreen video overflows screen in desktop mode (GeckoView) | S3 | NEW | 2025-11-22 |
| [2000214](https://bugzilla.mozilla.org/show_bug.cgi?id=2000214) | Horizontal fullscreen visual bug | -- | UNCONFIRMED | 2025-11-14 |
| [1844573](https://bugzilla.mozilla.org/show_bug.cgi?id=1844573) | White margin when entering fullscreen mode on most pages | S2 (regression) | NEW | 2024-07-09 |
| [1750416](https://bugzilla.mozilla.org/show_bug.cgi?id=1750416) | Fullscreen video cropped / incorrect size in GeckoView with ContentDelegate | S3 (regression) | NEW | 2025-02-11 |
| [1870999](https://bugzilla.mozilla.org/show_bug.cgi?id=1870999) | YouTube thumbnails overlapping in landscape mode | S3 | NEW | 2025-12-08 |

### Timeline Narrative

The oldest unresolved piece of this theme dates to January 2022 ([1750416](https://bugzilla.mozilla.org/show_bug.cgi?id=1750416), GeckoView fullscreen size regression, P3), indicating the problem has accumulated steadily. A regression in fullscreen white bars ([1844573](https://bugzilla.mozilla.org/show_bug.cgi?id=1844573)) was filed in mid-2023 and remains unaddressed at S2. Reports of orientation locking started appearing in Q3 2025, with three closely-related bugs filed October–January covering the landscape-lock-after-YouTube pattern. Bug 2003004 remains the most actively discussed (20 comments, last changed 2026-03-09), with multiple users confirming the behavior across different Android devices and Firefox versions. No meta bug has been formed and no engineer is assigned to any of these.

### Stagnation Callout

> **Stagnation:** [1750416](https://bugzilla.mozilla.org/show_bug.cgi?id=1750416) — S3 regression, last changed **2025-02-11** (over 13 months ago, well past the 90-day threshold). [1904654](https://bugzilla.mozilla.org/show_bug.cgi?id=1904654) — S3 regression, last changed **2025-07-03** (over 8 months ago). [1844573](https://bugzilla.mozilla.org/show_bug.cgi?id=1844573) — S2 regression, last changed **2024-07-09** (over 20 months ago with no resolution).

---

## Theme 2: Audio Playback Interrupted by System Events / Audio Focus Handling

### User-Facing Impact

Firefox loses audio playback state and fails to recover after Android system events like alarms, notifications, or phone calls interrupt audio focus. In the worst case (S2), users must force-quit and restart the app. The inverse failure also occurs: video/audio keeps playing even when Firefox is closed. Collectively these reflect poor integration with Android's `AudioManager` audio focus lifecycle.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2016829](https://bugzilla.mozilla.org/show_bug.cgi?id=2016829) | Android alarms stop Firefox from playing YouTube videos until app is force quit | S2 | NEW | 2026-03-18 |
| [1894494](https://bugzilla.mozilla.org/show_bug.cgi?id=1894494) | Playing list of audio files hangs after a while | S3 | NEW | 2026-02-03 |
| [1992980](https://bugzilla.mozilla.org/show_bug.cgi?id=1992980) | Notification badge persists on Realme devices after website plays audio | S3 | NEW | 2025-11-13 |
| [1975861](https://bugzilla.mozilla.org/show_bug.cgi?id=1975861) | Video in website keeps playing even after closing Firefox | S3 | NEW | 2025-10-09 |

### Timeline Narrative

Bug [2016829](https://bugzilla.mozilla.org/show_bug.cgi?id=2016829) arrived in February 2026 and was updated as recently as today (2026-03-18), making it the freshest S2 in the dataset. With 13 comments and active community engagement, it appears to be gaining traction. Bug [1894494](https://bugzilla.mozilla.org/show_bug.cgi?id=1894494) (audio hang) was filed May 2024 and received a flurry of activity in February 2026, suggesting a regression or newly affected hardware cohort. The Realme notification badge issue ([1992980](https://bugzilla.mozilla.org/show_bug.cgi?id=1992980)) has been triaged but remains unassigned for over four months.

### Stagnation Callout

> **Stagnation:** [1992980](https://bugzilla.mozilla.org/show_bug.cgi?id=1992980) — S3, triaged, last changed **2025-11-13** (>4 months, no assignee).

---

## Theme 3: Android Media Codec NDK Migration (Active Infrastructure Effort)

### User-Facing Impact

This theme is primarily developer-facing: Firefox is replacing its Java-based Android media codec stack with the Android NDK (Native Development Kit), affecting all native video/audio decoding and encoding on the platform. Users may experience improved codec performance and compatibility in future releases, but the migration also carries regression risk. Build toolchain friction (JDK 21 incompatibility with the old ExoPlayer module) and HLS playback via the legacy Java path are visible artifacts of this transition.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1980764](https://bugzilla.mozilla.org/show_bug.cgi?id=1980764) | [meta] Android Media Codec NDK implementation (70+ deps) | N/A | NEW (meta) | 2026-03-13 |
| [2004743](https://bugzilla.mozilla.org/show_bug.cgi?id=2004743) | Stop using Java media process for HLS | N/A | NEW | 2025-12-08 |
| [1997634](https://bugzilla.mozilla.org/show_bug.cgi?id=1997634) | Build fails with JDK 21 due to deprecated ExoPlayer source/target version | S3 | NEW | 2025-12-11 |
| [2001828](https://bugzilla.mozilla.org/show_bug.cgi?id=2001828) | ffmpeg av_send_packet/av_receive_frame loop indefinitely when buffers full | -- | ASSIGNED | (active) |
| [2023254](https://bugzilla.mozilla.org/show_bug.cgi?id=2023254) | Fix lifetimes for RemoteMediaDataEncoderChild and RemoteCDMChild | -- | ASSIGNED | (active) |

### Timeline Narrative

Meta bug [1980764](https://bugzilla.mozilla.org/show_bug.cgi?id=1980764) was filed August 2025 and has 70+ dependent bugs spanning encoding, decoding, ffmpeg integration, and HLS handoff. Active work is ongoing as of 2026-03-13 (last change time on the meta). Several sub-bugs were ASSIGNED to engineers (shravanrn, padenot, and others in the aosmond team) during the seed window. This is by far the most coordinated engineering effort visible in this dataset.

---

## Theme 4: Audio Decoder Crash — Active Topcrash

### User-Facing Impact

Firefox crashes while decoding audio during media playback. This is a top-ranked crash by volume (>1,000 occurrences per 30-day window) affecting Android users on the latest stable release channels (147–148). It crashes in the RDD or content process during audio time-stretching, likely triggered during seek or rate-change operations.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) | Crash in [@ mozilla::AudioDecoderInputTrack::EnsureTimeStretcher] | S2 | ASSIGNED — padenot@mozilla.com | 2026-03-16 |
| [1948620](https://bugzilla.mozilla.org/show_bug.cgi?id=1948620) | Crash in [@ mozilla::AudioDecoderInputTrack::EnsureTimeStretcher] (earlier instance) | S3 | RESOLVED | 2026-01-20 |

**Socorro Crash Volume:**

| Window | Count | Platform | Trend |
|--------|-------|----------|-------|
| 2026-01-15 to 2026-02-14 | 1,557 | Android only | — |
| 2026-02-15 to 2026-03-15 | 1,196 | Android only | Falling |
| Last 30 days | 1,290 | Android only | — |

- **Top versions:** 148.0.1 (410), 147.0.4 (301), 148.0.2 (220)
- **Process type:** Android (all reports)
- **Socorro signature:** [mozilla::AudioDecoderInputTrack::EnsureTimeStretcher](https://crashes.mozilla.org/signatures?q=signature%3A%22mozilla%3A%3AAudioDecoderInputTrack%3A%3AEnsureTimeStretcher%22)

### Timeline Narrative

The original crash was filed February 2025 ([1948620](https://bugzilla.mozilla.org/show_bug.cgi?id=1948620)) and resolved, but the crash resurfaced in January 2026 as a new bug ([2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539)) and received the `topcrash` keyword. Paul Adenot (:padenot) is actively working the fix as of 2026-03-16. The falling crash volume across the two windows (1,557 → 1,196) is an encouraging signal that a fix may be taking effect, though the crash has not yet been fully eliminated at 1,290/month.

---

## Theme 5: OpenSL Audio Stream Crash — Stagnant Crash

### User-Facing Impact

Firefox crashes in the parent process during OpenSL audio stream position queries (used by the cubeb audio backend). This affects users across a wide range of Android devices and has been producing hundreds of crash reports per month for well over a year, with no recent engineering activity.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1913284](https://bugzilla.mozilla.org/show_bug.cgi?id=1913284) | Crash in [@ libc.so \| opensl_stream_get_position] | S3 | NEW | 2025-03-05 |

**Socorro Crash Volume:**

| Window | Count | Platform | Process | Trend |
|--------|-------|----------|---------|-------|
| 2026-01-15 to 2026-02-14 | 710 | Android only | parent | — |
| 2026-02-15 to 2026-03-15 | 661 | Android only | parent | Stable |
| Last 30 days | 705 | Android only | parent | — |

- **Top version:** 143.0.4 (425 crashes in last 30d), also 147–148
- **Socorro signature:** [libc.so \| opensl_stream_get_position](https://crashes.mozilla.org/signatures?q=signature%3A%22libc.so%20%7C%20opensl_stream_get_position%22)

### Timeline Narrative

Bug [1913284](https://bugzilla.mozilla.org/show_bug.cgi?id=1913284) was filed in the Core::Audio/Video: cubeb component in August 2024. It has accumulated roughly 700 crash reports per month and shows no sign of resolving on its own — the trend is essentially flat. The preponderance on version 143.0.4 is unusual and may indicate a significant older-device cohort that is not auto-updating, or a platform-specific issue on certain Android API levels.

### Stagnation Callout

> **Stagnation:** [1913284](https://bugzilla.mozilla.org/show_bug.cgi?id=1913284) — S3 crash bug with **705 crashes/month**, last changed **2025-03-05** (over **12 months** without any activity). This should be escalated.

---

## Theme 6: WebRTC Camera Crashes

### User-Facing Impact

Firefox crashes or throws exceptions when users access the device camera for video calls or getUserMedia-based apps (e.g., video conferencing, QR code scanning). Multiple independent crash vectors and API failure modes have been reported across both Firefox for Android and GeckoView embedders.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1985792](https://bugzilla.mozilla.org/show_bug.cgi?id=1985792) | Crash in [@ java.lang.NullPointerException: at org.webrtc.CameraCapturer.createSessionInternal] | S3 | NEW | 2025-10-07 |
| [1979932](https://bugzilla.mozilla.org/show_bug.cgi?id=1979932) | Crash in [@ java.lang.RuntimeException: at org.webrtc.CameraSession.onShutdown] | S3 | NEW | 2025-12-04 |
| [2009725](https://bugzilla.mozilla.org/show_bug.cgi?id=2009725) | getUserMedia throws exception after stopping different camera stream tracks | S3 | UNCONFIRMED | 2026-02-18 |

**Socorro Crash Volume (from Fenix facet, last 30 days):**
- `java.lang.NullPointerException: at org.webrtc.CameraCapturer.createSessionInternal(CameraCapturer.java)`: **~613 crashes**
- **Signature link:** [CameraCapturer NullPointerException](https://crashes.mozilla.org/signatures?q=signature%3A%22java.lang.NullPointerException%3A+at+org.webrtc.CameraCapturer.createSessionInternal%28CameraCapturer.java%29%22)

### Timeline Narrative

Bug [1985792](https://bugzilla.mozilla.org/show_bug.cgi?id=1985792) filed August 2025 for the CameraCapturer NPE (the higher-volume crash) sits in Core::WebRTC: Audio/Video unassigned. The CameraSession RuntimeException ([1979932](https://bugzilla.mozilla.org/show_bug.cgi?id=1979932)) filed in July 2025 is separate but closely related, both involving org.webrtc lifecycle management. The getUserMedia API exception ([2009725](https://bugzilla.mozilla.org/show_bug.cgi?id=2009725)) was filed January 2026 against GeckoView, pointing to a race condition when stopping and starting camera streams. With ~613 monthly crashes and three independent reporter paths, this qualifies as a meaningful WebRTC quality gap.

---

## Theme 7: DRM/EME Content Restrictions (Emerging)

### User-Facing Impact

Some video streaming and cloud gaming services fail to play content on Firefox for Android and GeckoView. A related but distinct security concern involves EME/DRM permission prompts that display the wrong site origin (the top-level origin rather than the frame origin), which can mislead users into granting DRM permissions to the wrong context.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1841246](https://bugzilla.mozilla.org/show_bug.cgi?id=1841246) | EME/DRM iframe popup shows toplevel origin instead of frame origin | S2 | NEW | 2025-10-21 |
| [1962813](https://bugzilla.mozilla.org/show_bug.cgi?id=1962813) | Certain video and cloud game streaming services do not play content (GeckoView) | S2 | UNCONFIRMED | 2025-11-27 |
| [1912088](https://bugzilla.mozilla.org/show_bug.cgi?id=1912088) | daylightcomputer.com breaks with HLS disabled on Android | S4 | NEW (regression) | 2025-06-17 |

### Timeline Narrative

Bug [1841246](https://bugzilla.mozilla.org/show_bug.cgi?id=1841246) is the oldest S2 in the dataset (filed June 2023) and carries the `csectype-spoof` keyword — a security classification indicating the spoofing risk is acknowledged. Despite P2 priority and 34 comments, it remains unassigned. Bug [1962813](https://bugzilla.mozilla.org/show_bug.cgi?id=1962813) (GeckoView cloud gaming) is UNCONFIRMED, which means downstream GeckoView apps building video-game streaming products may be blocked. Both are S2 with no assignee.

### Stagnation Callout

> **Stagnation:** [1841246](https://bugzilla.mozilla.org/show_bug.cgi?id=1841246) — S2, P2, `csectype-spoof`, last changed **2025-10-21** (nearly 5 months ago). A security-classified S2 at P2 with no assignee warrants immediate attention.

---

## Emerging Issue: Erroneous Audio Permission Request on Image File Input

Bug [2002689](https://bugzilla.mozilla.org/show_bug.cgi?id=2002689) filed November 2025: Firefox for Android requests "Music and Audio on this device" permission when a user taps `<input type="file" accept="image/*">`. This is a confirmed regression (has the `regression` keyword), S3, with 13 comments confirming broad reproduction. The root cause likely involves incorrect MIME type handling leaking audio permissions into the file picker. Not yet a full theme (1 breadcrumb), but the regression nature and comment engagement suggest it will grow if not acted upon soon.

---

## Closing

### Ranked Signal Summary

| Rank | Theme | Breadcrumb Count | Meta Bug | Top Severity | Notes |
|------|-------|-----------------|----------|--------------|-------|
| 1 | Android Media Codec NDK Migration | 70+ (via meta) | [1980764](https://bugzilla.mozilla.org/show_bug.cgi?id=1980764) | N/A (infra) | Major coordinated effort, actively worked |
| 2 | Fullscreen Video & Orientation Dysfunction | 13 | None | S2 | Severe stagnation; no assignee on any bug |
| 3 | Audio Decoder Topcrash (EnsureTimeStretcher) | 3 | None | S2 | 1,290 crashes/month; ASSIGNED, falling trend |
| 4 | OpenSL Audio Crash | 2 (+Socorro) | None | S3 | 705 crashes/month, **12 months stagnant** |
| 5 | Audio Playback Interruption / Audio Focus | 4 | None | S2 | S2 bug filed 33 days ago, actively engaged |
| 6 | WebRTC/Camera Crashes | 3 (+Socorro) | None | S3 | ~613 crashes/month, unassigned |
| 7 | DRM/EME Content Restrictions | 3 | None | S2 | Security-classified S2 stagnant >5 months |

### Highlights to Watch

- **Bug [2016829](https://bugzilla.mozilla.org/show_bug.cgi?id=2016829)** (S2 alarm interrupts YouTube): Updated today — may be the fastest-moving item in this report. Worth triaging to P1/P2 if confirmed as audio focus regression.
- **Bug [1913284](https://bugzilla.mozilla.org/show_bug.cgi?id=1913284)** (OpenSL crash): The most egregious stagnation case — a crash bug with 700+ monthly reports that has had zero activity for a full year.
- **Theme 1 (Orientation/Fullscreen)**: 13 breadcrumbs, multiple S2/S3 regressions, zero assignees. A triage sprint or owning team designation would dramatically reduce the unresolved count.

### Resources Used

- **Bugzilla REST API:** ~14 queries (seed fetches, dep crawl, keyword expansion, batch lookups)
- **Socorro (socorro-cli):** 10+ queries (facet search, signature lookup, trend comparisons)
- **Dep crawl depth:** 2 levels (meta bug 1980764, crash bugs 2011539 / 1948620)
- **cc_count:** Not available via unauthenticated Bugzilla REST API; substituted with `comment_count`

### Suggestions for Improving This Skill

- Add a `--cc-threshold` filter option so the skill can surface bugs by cc_count even when the API requires auth (perhaps via a dedicated authenticated session or token)
- The `--no-mixed-seed` flag docs could mention that creation-time-only mode may miss long-lived high-engagement bugs that are still being actively commented on
- Consider a `--product-only` flag for the dep crawl to limit cross-component noise when the user's focus is purely on one product

---

*"The art of detection lies not in the obvious clues, but in the quiet patterns that persistently refuse to resolve themselves."*
