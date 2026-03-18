# Bugzilla Wrangler Report — Media (Core Audio/Video)

---

## Session Info

| Field | Value |
|---|---|
| **Date** | 2026-03-18 |
| **Scope** | `media` — Core: Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs, Web Audio |
| **Seed Timeframe** | 2025-12-18 → 2026-03-18 (last 3 months) |
| **Seed Count** | 50 |
| **Seed Mode** | mixed-seed (38 created + 12 changed = 50 unique) |
| **Cache Freshness** | Live fetch (default window — cache bypassed on read) |

---

## Seed Info

### Seed Bugs (by priority)

**P1 / S1-S2:**
- [2024007](https://bugzilla.mozilla.org/show_bug.cgi?id=2024007) — AssertedCast error: Cannot cast int64_t to float in FFmpegVideoDecoder (S2, P1, ASSIGNED) *(2026-03-17)*
- [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) — AppLocker Publisher rules don't work when loading DLLs with restricted access token (S3, P1, ASSIGNED) *(2026-03-13)*

**P2 / S2:**
- [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) — Crash in [@ syscall | std::sys::pal::unix::futex::futex_wait] (S2, P2, ASSIGNED) *(2026-03-12)*
- [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) — 28.4-15.12% ve-av1-q wallclock regression on OSX (S2, P2, NEW) *(2026-03-13)*
- [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) — [Meta] Bluetooth device related issues with audio and video (S2, P2, NEW) *(2026-01-21)*
- [2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568) — Use a single rlbox sandbox for all soundtouch instances (S2, P2, NEW) *(2026-03-16)*
- [2023515](https://bugzilla.mozilla.org/show_bug.cgi?id=2023515) — Crash in [@ libc.so | libmozglue.so | libart.so | JNI Method::Call] (S2, P2, NEW) *(2026-03-16)*
- [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) — Crash in [@ mozilla::AudioDecoderInputTrack::EnsureTimeStretcher] (S2, P2, ASSIGNED, topcrash) *(2026-01-20)*
- [2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567) — Handle more TimeUnit overflow cases in MSE (S3, P2, NEW) *(2026-02-18)*
- [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) — High-bitrate AV1 freezes: DAV1DDecoder busy-waits on dav1d EAGAIN (S2, P2, NEW) *(2026-02-12)*
- [2016501](https://bugzilla.mozilla.org/show_bug.cgi?id=2016501) — crash at null in [@ mozilla::EncoderAgent::Dry] (S3, P2, NEW) *(2026-02-12)*

**P3 / S3:**
- [2021805](https://bugzilla.mozilla.org/show_bug.cgi?id=2021805) — Firefox mutes YouTube video when Wheel-Clicking a Tweet (S3, P3, UNCONFIRMED) *(2026-03-08)*
- [2023447](https://bugzilla.mozilla.org/show_bug.cgi?id=2023447) — High power consumption and heat when playing YouTube videos (S3, P3, UNCONFIRMED) *(2026-03-15)*
- [2013720](https://bugzilla.mozilla.org/show_bug.cgi?id=2013720) — Screen saver activates when streaming video in Firefox on Linux Mint (S3, P3, UNCONFIRMED) *(2026-01-31)*
- [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) — [meta] Media Related Sleep Issues (S3, P3, NEW) *(2026-03-14)*
- [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) — Nvidia Tegra Video HW Decoding Regression with Firefox 142+ (S3, P3, NEW, regression) *(2026-02-12)*
- [2020653](https://bugzilla.mozilla.org/show_bug.cgi?id=2020653) — Disconnecting AirPods no longer pauses media on YouTube (S3, P3, UNCONFIRMED) *(2026-03-03)*
- [2009171](https://bugzilla.mozilla.org/show_bug.cgi?id=2009171) — Intermittent freeze after Bluetooth disconnect on Windows 11 (S3, P3, UNCONFIRMED) *(2026-01-08)*
- [2008781](https://bugzilla.mozilla.org/show_bug.cgi?id=2008781) — Bluetooth audio stuttering when playing a video (S3, P3, UNCONFIRMED) *(2026-01-06)*
- [2009596](https://bugzilla.mozilla.org/show_bug.cgi?id=2009596) — [HDR/Windows] Intel Iris Xe doesn't show HDR video (S3, P3, NEW) *(2026-01-11)*
- [2009624](https://bugzilla.mozilla.org/show_bug.cgi?id=2009624) — HDR transfer function mismatch on Qualcomm Snapdragon X1 (S3, P3, NEW) *(2026-01-11)*
- [2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122) — HEVC video doesn't play in flatpak builds (S3, P3, NEW) *(2026-03-04)*
- [2020823](https://bugzilla.mozilla.org/show_bug.cgi?id=2020823) — h264 video not decoded with hardware in flatpak build (S3, P3, NEW) *(2026-03-03)*
- [2018819](https://bugzilla.mozilla.org/show_bug.cgi?id=2018819) — No way to add exceptions to Autoplay default permissions (S3, P3, UNCONFIRMED) *(2026-02-24)*
- [2007762](https://bugzilla.mozilla.org/show_bug.cgi?id=2007762) — Audio/video desync when toggling playback speed (Arch Linux/PipeWire) (S3, P3, NEW) *(2025-12-26)*
- [2020532](https://bugzilla.mozilla.org/show_bug.cgi?id=2020532) — Strange msgs at FF startup (cubeb) (S3, P3, UNCONFIRMED) *(2026-03-03)*
- [2012285](https://bugzilla.mozilla.org/show_bug.cgi?id=2012285) — [NVIDIA] Fails to create headless HW accelerated GL context (S3, P3, UNCONFIRMED) *(2026-01-24)*
- [2017271](https://bugzilla.mozilla.org/show_bug.cgi?id=2017271) — Video choppy on Coursera.org after 12 hours (S3, --, NEW) *(2026-02-17)*
- [2016952](https://bugzilla.mozilla.org/show_bug.cgi?id=2016952) — Crash in [@ OOM | small] (S3, --, UNCONFIRMED) *(2026-02-14)*
- [2018005](https://bugzilla.mozilla.org/show_bug.cgi?id=2018005) — Firefox crashes gnome desktop (SIGSEGV) (S3, --, UNCONFIRMED) *(2026-02-19)*
- [2023254](https://bugzilla.mozilla.org/show_bug.cgi?id=2023254) — Fix lifetimes for RemoteMediaDataEncoderChild and RemoteCDMChild (S3, --, ASSIGNED) *(2026-03-13)*
- [2023046](https://bugzilla.mozilla.org/show_bug.cgi?id=2023046) — Ogg file crafted with JS causes release assertion crash (S3, P3, NEW) *(2026-03-13)*
- [2009944](https://bugzilla.mozilla.org/show_bug.cgi?id=2009944) — Intermittent: MOZ_CRASH(Plugin file does not exist) in GMPChild.cpp (S4, P5) *(2026-01-13)*
- [2018116](https://bugzilla.mozilla.org/show_bug.cgi?id=2018116) — Intermittent crashtest timeout (intermittent-failure, regression) (S4, P5) *(2026-02-20)*
- [2007252](https://bugzilla.mozilla.org/show_bug.cgi?id=2007252) — Intermittent Assertion failure: native || Switching() in MediaTrackGraph.cpp (S4, P5) *(2025-12-20)*
- [2020664](https://bugzilla.mozilla.org/show_bug.cgi?id=2020664) — Intermittent gtest TestWebrtcGmpVideoEncoder.Encode (S4, P5) *(2026-03-03)*
- [2010150](https://bugzilla.mozilla.org/show_bug.cgi?id=2010150) — Intermittent ASan SEGV in MOZ_CrashSequence (S4, P5) *(2026-01-13)*
- [2021505](https://bugzilla.mozilla.org/show_bug.cgi?id=2021505) — Check bit depth for codec (S4, P5, NEW) *(2026-03-06)*

**From Query B (recently changed, pre-window creation):**
- [1916629](https://bugzilla.mozilla.org/show_bug.cgi?id=1916629) — Crash in [@ mio::sys::windows::named_pipe::read_done] (S3, P2, ASSIGNED, topcrash, regression) *(created 2024-09-04)*
- [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317) — Move Cubeb processing to a utility process (Windows) (S3, --, ASSIGNED) *(created 2024-05-28)*
- [1985126](https://bugzilla.mozilla.org/show_bug.cgi?id=1985126) — Mono audio via external DAC outputs only from left channel (S3, P3, ASSIGNED) *(created 2025-08-25)*
- [1903051](https://bugzilla.mozilla.org/show_bug.cgi?id=1903051) — Massive parent process jank hovering over video in Google Drive (S3, --, NEW) *(created 2024-06-17)*
- [1973534](https://bugzilla.mozilla.org/show_bug.cgi?id=1973534) — HDMI audio cuts off after 1-2 seconds (AMD, Windows 11) (S3, P3, ASSIGNED) *(created 2025-06-23)*
- [1997237](https://bugzilla.mozilla.org/show_bug.cgi?id=1997237) — YouTube won't play videos in private window after browsing yahoo.com (S3, P3, UNCONFIRMED) *(created 2025-10-30)*
- [1972665](https://bugzilla.mozilla.org/show_bug.cgi?id=1972665) — Audio dies when switching audio tracks (Widevine, Desktop) (S3, P3, UNCONFIRMED, 12 comments) *(created 2025-06-17)*
- [1997480](https://bugzilla.mozilla.org/show_bug.cgi?id=1997480) — Crash in [@ moz_wasm2c_memgrow_failed] (S3, P3, NEW) *(created 2025-10-31)*
- [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) — x.com causes audio interface to be opened (PipeWire) despite nothing playing (S3, P2, NEW) *(created 2025-08-24)*
- [2005868](https://bugzilla.mozilla.org/show_bug.cgi?id=2005868) — Frequent ThreadSanitizer SEGV in MOZ_CrashSequence (S4, P5, intermittent-failure, 40 comments) *(created 2025-12-13)*
- [1959613](https://bugzilla.mozilla.org/show_bug.cgi?id=1959613) — Audio stream remains open when playback paused (S4, --, UNCONFIRMED) *(created 2025-04-10)*
- [1999168](https://bugzilla.mozilla.org/show_bug.cgi?id=1999168) — VideoDecoder.isConfigSupported() returns false for HEVC despite HW decoding available (S3, P3, NEW) *(created 2025-11-10)*

### Creation Date Distribution

Seeds created in the 3-month window (Dec 2025 – Mar 2026):

```
Dec 2025  [ ##                              ]  2 bugs  (2007252, 2007762)
Jan 2026  [ ##########                      ] 10 bugs  (2008781, 2009171, 2009596, 2009624, 2009944,
                                                         2010150, 2011539, 2011679, 2012285, 2013720)
Feb 2026  [ ########                        ]  8 bugs  (2016484, 2016501, 2016587, 2017271, 2017567,
                                                         2018005, 2018116, 2018819)
Mar 2026  [ ###############                 ] 15 bugs  (2020532, 2020653, 2020823, 2021122, 2021505,
                                                         2021805, 2023046, 2023094, 2023159, 2023254,
                                                         2023379, 2023447, 2023515, 2023568, 2024007)
(+12 older bugs recently changed, not shown in timeline)
```

The seed skews toward late-January and March, which aligns with Firefox 148 pre-release activity and the media bug intake pattern. December coverage is sparse (holiday period).

---

## Theme 1: Windows Audio IPC — mio Named Pipe Crash

**User-facing impact:** Firefox crashes silently in the content or utility process when using audio on Windows. The crash occurs in the Rust mio IPC layer used by the audio backend. Users lose audio entirely and may experience tab crashes or process restarts. Affects Windows 10 and 11 across all release channels (release, beta, ESR).

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [1916629](https://bugzilla.mozilla.org/show_bug.cgi?id=1916629) | Crash in [@ mio::sys::windows::named_pipe::read_done] | S3 | ASSIGNED (ChunMinChang) | 2026-03-18 |
| [2024485](https://bugzilla.mozilla.org/show_bug.cgi?id=2024485) | Update mio to 1.1.1 (fix) | -- | ASSIGNED | 2026-03-18 |
| [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317) | Move Cubeb processing to a utility process (Windows) | S3 | ASSIGNED | 2026-03-18 |
| [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) | Rework AudioIPC initialization to avoid blocking parent main thread | -- | ASSIGNED | 2026-03-18 |

### Crash Volume

| Metric | Value |
|--------|-------|
| **Crash Volume (30d)** | **1,104 crashes** (default socorro window — all on Windows) |
| **Top Platform** | Windows NT 10.0 (Win10/Win11 — 100%) |
| **Affected Versions** | Release 148.0.2, Beta 149.0b8, ESR 140.7/140.8 |
| **Trend** | Active — date-filtered queries timed out, but high absolute volume confirmed |

Socorro: [mio::sys::windows::named_pipe::read_done](https://crashes.mozilla.org/signatures?q=signature%3A%22mio%3A%3Asys%3A%3Awindows%3A%3Anamed_pipe%3A%3Aread_done%22)

### Timeline Narrative

This crash was first filed in September 2024, surfacing as a consequence of the ongoing effort to move cubeb audio processing out of the Firefox parent process and into a utility process (bug [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317)). The IPC between processes uses the Rust `mio` crate's named pipe implementation on Windows, and a bug in the older mio version causes a crash in `read_done`. The fix is straightforward — update mio from the current version to 1.1.1 (bug [2024485](https://bugzilla.mozilla.org/show_bug.cgi?id=2024485)). Both fix bugs were opened on 2026-03-18 and are actively ASSIGNED. The simultaneous opening of [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) ("Rework AudioIPC initialization") suggests related architectural cleanup is in-flight.

With 1,104 crash reports, this is the highest-volume crash in the seed window and is the primary driver for immediate attention. The fix is in motion but not yet landed.

---

## Theme 2: Bluetooth Audio/Video Issues

**User-facing impact:** Users with Bluetooth headphones, earbuds (AirPods, Pixel Buds, Bose), or speakers experience audio stuttering, desync, muting, pausing, or complete silence when using Firefox. The problem is worse on video-heavy sites (YouTube) and is triggered by device connect/disconnect events, ad playback, or background tab activity. Affects all major platforms: Windows, Android, macOS, and Linux.

### Breadcrumb Table (key bugs — 23 total deps in meta)

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) | [Meta] Bluetooth device related issues with audio and video | S2 | NEW | 2026-03-18 |
| [1835986](https://bugzilla.mozilla.org/show_bug.cgi?id=1835986) | Audio and video stutter with Bluetooth on Android 13 (Firefox) | S3 | NEW (P2, 28 comments) | — |
| [1936931](https://bugzilla.mozilla.org/show_bug.cgi?id=1936931) | Video desyncs with audio after YouTube ads if BT headphones used | S3 | UNCONFIRMED (P2) | — |
| [1937317](https://bugzilla.mozilla.org/show_bug.cgi?id=1937317) | Videos stop when headphones removed (regression keyword) | S3 | NEW (P2) | — |
| [1973353](https://bugzilla.mozilla.org/show_bug.cgi?id=1973353) | Delayed video start/resume by Bluetooth | S2 | UNCONFIRMED (P3) | — |
| [1888896](https://bugzilla.mozilla.org/show_bug.cgi?id=1888896) | A2DP/HSP+HFP Bluetooth profile switching issues | S3 | NEW (P3) | — |
| [2009171](https://bugzilla.mozilla.org/show_bug.cgi?id=2009171) | Intermittent freeze after BT disconnect on Windows 11 | S3 | UNCONFIRMED (P3) | 2026-03-05 |
| [2020653](https://bugzilla.mozilla.org/show_bug.cgi?id=2020653) | Disconnecting AirPods no longer pauses media (YouTube) | S3 | UNCONFIRMED (P3) | 2026-03-14 |
| [2008781](https://bugzilla.mozilla.org/show_bug.cgi?id=2008781) | Bluetooth audio stuttering when playing a video | S3 | UNCONFIRMED (P3) | 2026-03-04 |
| [1987257](https://bugzilla.mozilla.org/show_bug.cgi?id=1987257) | AirPods Pro 2 desync between left/right earbuds (macOS 15) | S3 | UNCONFIRMED (P3) | — |
| [1957088](https://bugzilla.mozilla.org/show_bug.cgi?id=1957088) | sesame.com: AI voice demo silent with BT headphones | S3 | NEW (P3) | — |
| [2021805](https://bugzilla.mozilla.org/show_bug.cgi?id=2021805) | Firefox mutes YouTube for a second on Wheel-Click of a tweet | S3 | UNCONFIRMED (P3) | 2026-03-17 |
| [1990361](https://bugzilla.mozilla.org/show_bug.cgi?id=1990361) | Audio cut when using Bluetooth headset | S3 | NEW (P3) | — |
| [1868267](https://bugzilla.mozilla.org/show_bug.cgi?id=1868267) | Desynced audio channels with Bluetooth AirPods on play/pause | S3 | UNCONFIRMED | — |

### Timeline Narrative

Bluetooth-related audio issues have accumulated in Bugzilla since at least bug [1492488](https://bugzilla.mozilla.org/show_bug.cgi?id=1492488) (filed 2018). The meta bug [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) was created on 2026-01-21 to unify 23 disparate reports. The meta itself carries S2/P2 and was last touched on 2026-03-18 (same day as the mio fix work), suggesting active awareness. However, the meta has no assigned engineer and no blocking dependency graph that would indicate active engineering effort.

The root problems appear to be: (1) cubeb's handling of device change events on each platform (Windows: WASAPI device changes; macOS: CoreAudio endpoint changes; Linux: PipeWire source re-routing; Android: AudioTrack device switches) and (2) Firefox's lack of native media session integration to respond to hardware media buttons and device events. The overlap with the sleep/power theme is high — many disconnect events occur during screen lock or sleep.

> **Stagnation callout:** The meta bug [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) (S2, P2) is NEW with no assignee and no blocking engineering work. Multiple S3 deps have had no activity in >30 days. This is a recognized collection of issues with no clear ownership.

---

## Theme 3: Media Sleep/Wake/Power Issues

**User-facing impact:** Firefox interferes with system power management in both directions: (1) video playback fails to prevent display sleep, causing the screen saver to kick in during films, and (2) Firefox incorrectly holds the audio device open even when nothing is playing, preventing the system from sleeping or draining the battery. After system wake, audio or video often fails to resume. Affects Linux (PipeWire, X11), macOS, and Windows.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) | [meta] Media Related Sleep Issues (16 deps) | S3 | NEW | 2026-03-15 |
| [2013720](https://bugzilla.mozilla.org/show_bug.cgi?id=2013720) | Screen saver activates when streaming video (Linux Mint) | S3 | UNCONFIRMED | 2026-03-16 |
| [2023447](https://bugzilla.mozilla.org/show_bug.cgi?id=2023447) | High power consumption and heat playing YouTube | S3 | UNCONFIRMED | 2026-03-16 |
| [1821102](https://bugzilla.mozilla.org/show_bug.cgi?id=1821102) | Firefox keeps coreaudiod active, prevents sleep on macOS | S3 | UNCONFIRMED (P3) | — |
| [1851996](https://bugzilla.mozilla.org/show_bug.cgi?id=1851996) | Audio prevents PC from sleep | S3 | UNCONFIRMED | — |
| [1984927](https://bugzilla.mozilla.org/show_bug.cgi?id=1984927) | Display goes to sleep while watching YouTube | S3 | NEW (P3) | — |
| [1913428](https://bugzilla.mozilla.org/show_bug.cgi?id=1913428) | Fullscreen video doesn't trigger system sleep timer suppression | S3 | UNCONFIRMED | — |
| [1977132](https://bugzilla.mozilla.org/show_bug.cgi?id=1977132) | Media playback auto-resumes on Windows lock screen after wake | S3 | NEW (P3) | — |
| [1961596](https://bugzilla.mozilla.org/show_bug.cgi?id=1961596) | Unmuted video doesn't play after computer sleep on macOS | S3 | UNCONFIRMED (P3) | — |
| [1519935](https://bugzilla.mozilla.org/show_bug.cgi?id=1519935) | Windows sleep causes video to stop after wake | S3 | NEW (P3) | — |
| [1606331](https://bugzilla.mozilla.org/show_bug.cgi?id=1606331) | Netflix: video continues after sleep but audio is lost | S3 | NEW (P3) | — |
| [1959613](https://bugzilla.mozilla.org/show_bug.cgi?id=1959613) | Audio stream remains open when playback paused (cubeb) | S4 | UNCONFIRMED | 2026-03-18 |

### Timeline Narrative

The meta bug [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) was created on 2026-03-14 — very recent — indicating someone recently recognized this as a cluster worth tracking. It already has 16 deps spanning bugs filed as far back as 2019. The issues fall into two camps: (a) Firefox not registering with the OS inhibitor API correctly to prevent sleep during fullscreen video, and (b) the audio device being held open unnecessarily (related to cubeb's `1959613`). Some deps are also in the Bluetooth cluster (device reconnect after sleep fails). No engineer is assigned and the meta is at P3.

The `1959613` bug (audio stream open during pause) also surfaced in the recently-changed query, suggesting active interest in it during this period.

> **Stagnation callout:** Many S3 bugs in this meta have had no activity for >90 days and predate Firefox 100. The new meta is a positive sign but does not yet have an assigned owner.

---

## Theme 4: AV1 Decoding Regressions and Performance Issues

**User-facing impact:** AV1 video — now the dominant codec on YouTube, Netflix, and streaming platforms — is degraded in multiple ways: high-bitrate streams freeze (the decoder busy-waits instead of draining frames), a macOS performance regression causes wallclock slowdowns, and AMD GPU users see 4K freezes. These are often silent: the page appears stuck with no error message.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) | High-bitrate AV1 freezes: DAV1DDecoder busy-waits on EAGAIN | S2 | NEW | 2026-03-15 |
| [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) | 28.4-15.12% ve-av1-q wallclock regression on macOS (Mon Mar 9 2026) | S2 | NEW | 2026-03-18 |
| [2024007](https://bugzilla.mozilla.org/show_bug.cgi?id=2024007) | AssertedCast error: Cannot cast int64_t to float in FFmpegVideoDecoder | S2 | ASSIGNED | 2026-03-18 |
| [1978703](https://bugzilla.mozilla.org/show_bug.cgi?id=1978703) | AV1 video stuttering with media.ffvpx-hw.enabled=true | S3 | REOPENED (P2) | — |
| [1884529](https://bugzilla.mozilla.org/show_bug.cgi?id=1884529) | [AMD RX 6700 XT] 4K AV1 on YouTube freezes | S3 | UNCONFIRMED (P3) | — |
| [2008617](https://bugzilla.mozilla.org/show_bug.cgi?id=2008617) | 4K AV1 video decode doesn't work on YouTube | S3 | UNCONFIRMED (P3) | — |

### Timeline Narrative

The P1/S2 regression [2024007](https://bugzilla.mozilla.org/show_bug.cgi?id=2024007) was filed on 2026-03-17 and is already ASSIGNED — it involves an `AssertedCast` overflow in `FFmpegVideoDecoder::DecodeStats::UpdateDecodeTimes`, likely triggered by very long videos or large decode timestamps. Separately, the macOS AV1 performance regression [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) surfaced from PerfAlert on 2026-03-13, tied to Mon March 9 2026 (a specific landing).

The longer-standing [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) (DAV1D busy-wait) is S2/P2 and has been open since February 2026 without assignment. The `DAV1DDecoder::InvokeDecode` busy-waits on `EAGAIN` instead of draining queued frames — a correctness bug in the decoder loop.

Combined, these three S2 bugs paint a picture of the AV1 decode path under pressure.

---

## Theme 5: cubeb Linux/Unix Audio Issues

**User-facing impact:** On Linux (especially PipeWire), Firefox has persistent audio device management problems: the audio device is opened by pages that aren't playing audio, stays open when paused, produces desync when playback speed is changed, and can crash. A separate S2 crash in the cubeb futex path affects Linux ESR users.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) | Crash in [@ syscall \| futex::futex_wait] (cubeb utility process) | S2 | ASSIGNED | 2026-03-18 |
| [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) | Rework AudioIPC initialization (fix for 2022993 / 1899317) | -- | ASSIGNED | 2026-03-18 |
| [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) | x.com opens audio interface (PipeWire) despite nothing playing | S3 | NEW (P2) | 2026-03-18 |
| [1973534](https://bugzilla.mozilla.org/show_bug.cgi?id=1973534) | HDMI audio cuts off after 1-2 seconds (AMD, Windows 11) | S3 | ASSIGNED (P3) | 2026-03-18 |
| [2007762](https://bugzilla.mozilla.org/show_bug.cgi?id=2007762) | Audio/video desync when toggling playback speed (PipeWire) | S3 | NEW (P3) | 2026-03-15 |
| [1985126](https://bugzilla.mozilla.org/show_bug.cgi?id=1985126) | Mono audio via external DAC only plays from left channel | S3 | ASSIGNED (P3) | 2026-03-18 |
| [1959613](https://bugzilla.mozilla.org/show_bug.cgi?id=1959613) | Audio stream remains open when playback paused | S4 | UNCONFIRMED | 2026-03-18 |
| [1903051](https://bugzilla.mozilla.org/show_bug.cgi?id=1903051) | Massive parent process jank hovering over video in Google Drive | S3 | NEW | 2026-03-18 |

### Crash Volume (2022993 signature)

| Metric | Value |
|--------|-------|
| **Crash Volume (30d)** | **52 crashes** |
| **Top Platform** | Linux (100% of reports) |
| **Affected Versions** | Release 148.0.2, ESR 140.7/140.8 |
| **Trend** | Stable (present on ESR, suggesting pre-existing) |

Socorro: [syscall | std::sys::pal::unix::futex::futex_wait](https://crashes.mozilla.org/signatures?q=signature%3A%22syscall+%7C+std%3A%3Asys%3A%3Apal%3A%3Aunix%3A%3Afutex%3A%3Afutex_wait%22)

### Timeline Narrative

The futex crash [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) and the AudioIPC initialization rework [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) were both opened on 2026-03-18 and are immediately ASSIGNED — this is active engineering work. The root cause appears to be a race condition in the new cubeb utility process IPC initialization on Unix. Bug [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317) (the underlying utility process move for Windows) is the architectural parent.

Separately, [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) (P2) highlights a latency-sensitive issue: x.com's Web Audio use opens the PipeWire audio interface even with the tab muted and nothing playing, causing audible device activation events for users with hardware indicators. This is a correctness issue in how lazy audio context initialization interacts with PipeWire.

---

## Theme 6: MSE and Codec Arithmetic Safety

**User-facing impact:** A cluster of arithmetic safety bugs — integer overflows, out-of-range casts, and negative-value assertions — in the MSE (Media Source Extensions) and codec layers. Most affect long-running sessions or unusual media inputs. Users see either silent crashes or stuck playback.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2024007](https://bugzilla.mozilla.org/show_bug.cgi?id=2024007) | AssertedCast: Cannot cast int64_t to float in FFmpegVideoDecoder | S2 | ASSIGNED (P1, regression) | 2026-03-18 |
| [2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567) | Handle more TimeUnit overflow cases in MSE | S3 | NEW (P2) | 2026-03-17 |
| [2023046](https://bugzilla.mozilla.org/show_bug.cgi?id=2023046) | Ogg JS-crafted file: negative timeDenom accepted, crashes release assertion | S3 | NEW (P3, csectype-dos) | 2026-03-18 |
| [2016501](https://bugzilla.mozilla.org/show_bug.cgi?id=2016501) | crash at null in [@ mozilla::EncoderAgent::Dry] | S3 | NEW (P2, crash) | 2026-03-10 |

### Timeline Narrative

These four bugs represent a pattern rather than a single root cause. The shared thread is insufficient bounds checking on integer arithmetic in media decode and encode paths: timestamps exceeding float range ([2024007](https://bugzilla.mozilla.org/show_bug.cgi?id=2024007)), TimeUnit arithmetic overflowing in MSE ([2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567)), and a security-adjacent DOS via malformed Ogg content ([2023046](https://bugzilla.mozilla.org/show_bug.cgi?id=2023046), flagged `csectype-dos`).

The P1 regression [2024007](https://bugzilla.mozilla.org/show_bug.cgi?id=2024007) is actively being fixed. [2023046](https://bugzilla.mozilla.org/show_bug.cgi?id=2023046) is externally reported (keyword `reporter-external`) and could use security triage attention.

---

## Theme 7: Hardware Video Decoding — Platform Gaps (Flatpak, HDR, NVIDIA)

**User-facing impact:** Hardware video acceleration fails silently on several platform configurations: Linux flatpak/sandbox builds cannot decode h264 or HEVC, Intel Iris Xe and Qualcomm Snapdragon X1 GPUs fail to play HDR video on Windows, and Nvidia Tegra hardware regressed in Firefox 142+. Users fall back to software decoding without feedback, causing high CPU usage and battery drain.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2020823](https://bugzilla.mozilla.org/show_bug.cgi?id=2020823) | h264 not decoded with hardware in flatpak build | S3 | NEW (P3) | 2026-03-11 |
| [2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122) | HEVC video doesn't play in flatpak builds | S3 | NEW (P3) | 2026-03-11 |
| [2009596](https://bugzilla.mozilla.org/show_bug.cgi?id=2009596) | [HDR/Windows] Intel Iris Xe (Alder Lake) doesn't show HDR video | S3 | NEW (P3) | 2026-03-16 |
| [2009624](https://bugzilla.mozilla.org/show_bug.cgi?id=2009624) | HDR video transfer function mismatch on Qualcomm Snapdragon X1 | S3 | NEW (P3) | 2026-03-12 |
| [2012285](https://bugzilla.mozilla.org/show_bug.cgi?id=2012285) | [NVIDIA] Fails to create headless HW accelerated GL context | S3 | UNCONFIRMED (P3, 22 comments) | 2026-03-05 |
| [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) | Nvidia Tegra Video HW Decoding Regression (Firefox 142+) | S3 | NEW (P3, regression) | 2026-03-15 |
| [1999168](https://bugzilla.mozilla.org/show_bug.cgi?id=1999168) | VideoDecoder.isConfigSupported() returns false for HEVC despite HW available | S3 | NEW (P3) | 2026-03-17 |

### Timeline Narrative

The flatpak bugs ([2020823](https://bugzilla.mozilla.org/show_bug.cgi?id=2020823), [2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122)) both point to `1867638` as a parent — the overall flatpak codec support tracking bug. Both were filed in early March 2026 and share the same symptom: hardware acceleration APIs are unavailable in the flatpak sandbox. The HDR issues are distinct: Intel [2009596](https://bugzilla.mozilla.org/show_bug.cgi?id=2009596) and Qualcomm [2009624](https://bugzilla.mozilla.org/show_bug.cgi?id=2009624) both block bug `2012848` (HDR meta). No assignees on any of these. The NVIDIA Tegra regression [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) has been open since February with a `regressionwindow-wanted` keyword, suggesting no one has identified the causative commit.

> **Stagnation callout:** All 7 bugs in this theme have had no activity in >7 days, and several (2009596, 2009624) have been stagnant since January 2026 with no assignee. The HDR meta bug `2012848` may need a re-prioritization pass.

---

## Emerging Theme: Android JNI Media Crash

**Why notable:** Two independently filed S2 bugs both point to Android-specific media failures that are distinct from the Bluetooth cluster. One is a crash (2023515), the other a broader test-infrastructure failure on Android 14 emulators. With Android's growing market share in Firefox's user base, even a limited signal in this area deserves monitoring.

### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023515](https://bugzilla.mozilla.org/show_bug.cgi?id=2023515) | Crash in [@ libc.so | libmozglue.so | libart.so | JNI Method::Call] | S2 | NEW (P2) | 2026-03-16 |
| [1984064](https://bugzilla.mozilla.org/show_bug.cgi?id=1984064) | New Android 14 emulator has many mochitest media failures on debug | S2 | ASSIGNED (P2) | 2026-03-17 |

**Note:** Only 2 breadcrumbs — below the 3-breadcrumb threshold for ranked themes. Flagging as emerging because of dual S2 severity and the JNI crash being externally observable.

---

## Closing

### Ranked Signal Summary

| Rank | Theme | Breadcrumbs | Meta Bug | Top Severity | Notes |
|------|-------|-------------|----------|--------------|-------|
| 1 | Windows Audio IPC — mio Named Pipe Crash | 4 | No | S3 | **1,104 crash reports**; fix ASSIGNED (mio 1.1.1 update + AudioIPC rework) |
| 2 | Bluetooth Audio/Video Issues | 25+ | [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) | S2 | 23 deps, no assignee, cross-platform, long-standing |
| 3 | Media Sleep/Wake/Power Issues | 18+ | [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) | S3 | New meta (Mar 14), 16 deps, no assignee |
| 4 | AV1 Decoding Regressions | 6 | No | S2 | Two S2 regressions + one S2 perf regression all active in March |
| 5 | cubeb Linux/Unix Audio Issues | 8 | No | S2 | Futex crash (52 reports) with fix in progress; PipeWire correctness gaps |
| 6 | MSE/Codec Arithmetic Safety | 4 | No | S2 | P1 regression being fixed; csectype-dos bug needs security triage |
| 7 | HW Video Decoding Platform Gaps | 7 | Partial (HDR meta 2012848) | S3 | All stagnant; Flatpak + HDR + Tegra regression unowned |
| E | Android JNI Media Crash | 2 | No | S2 | Below threshold — emerging |

### Resources Used

- **Bugzilla REST API:** 7 fetch calls (seed queries A+B, Bluetooth meta deps, sleep meta deps, dep bug details, cc_count, webcompat site-report expansion, AV1 keyword search)
- **socorro-cli:** 6 queries (mio crash, EnsureTimeStretcher, futex, mio date trend attempts, mio facets)
- **Tools:** WebFetch, Bash (socorro-cli)
- **Note:** cc_count fields were not returned by the Bugzilla REST API for these bugs (likely requires authentication); signal scoring for cc_count was omitted. Date-windowed socorro queries returned empty results — likely a CLI date-filter syntax issue; absolute crash volumes from default-window searches were used instead.

### Suggestions for Improving This Skill

- **cc_count fallback:** When `cc_count` is not returned by the REST API, consider fetching the bug page HTML and extracting it, or removing cc_count from the scoring rubric if it's consistently unavailable without auth.
- **Socorro date trend:** Document the correct `--date` flag syntax for windowed queries. The current syntax `--date ">=YYYY-MM-DD" --date "<YYYY-MM-DD"` appears to produce empty results — a known two-flag interaction issue. Use `--date ">=YYYY-MM-DD"` alone for "since" queries.
- **Dep crawl depth signal:** The skill currently caps dep crawl at depth 5 but for large meta bugs (23+ deps) some potentially important breadcrumbs get discarded. Consider allowing depth-1 full crawl on meta bugs by default.
- **Android scope integration:** Some Bluetooth/sleep bugs crossed into `Firefox for Android` component but the `media` scope only covers `Core`. A `media-android` scope combining both would catch cross-component themes earlier.

---

*"The art of finding clues is in knowing which doors to open — and which noise to ignore."*
