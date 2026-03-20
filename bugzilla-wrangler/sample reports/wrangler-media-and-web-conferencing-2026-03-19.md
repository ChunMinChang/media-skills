# Bugzilla Wrangler Report: media-and-web-conferencing

## Session Info

- **Date:** 2026-03-19
- **Scope:** media-and-web-conferencing
- **Components:** Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs, Web Audio, WebRTC, WebRTC: Audio/Video, WebRTC: Networking, WebRTC: Signaling
- **Seed timeframe:** 2025-12-19 to 2026-03-19
- **Seed count:** 46 (after filtering 4 intermittent-failure bugs)
- **Seed mode:** mixed-seed (38 created + 12 changed = 50 raw, 46 after filter)
- **Cache freshness:** Live fetch

---

## Seed Info

### Seed Bugs by Priority

**P1 / S2 (highest urgency)**
- [2024007](https://bugzilla.mozilla.org/show_bug.cgi?id=2024007) — AssertedCast error: Cannot cast int64_t to float in FFmpegVideoDecoder::DecodeStats::UpdateDecodeTimes — Audio/Video: Playback — S2/P1 ASSIGNED
- [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) — AppLocker Publisher rules don't work with USER_RESTRICTED token when loading DLLs — Audio/Video: GMP — S3/P1 ASSIGNED

**P2 / S2**
- [2023970](https://bugzilla.mozilla.org/show_bug.cgi?id=2023970) — about:support can leak PII via audio device names — Web Audio — S2/P2 NEW
- [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) — High-bitrate AV1 freezes: DAV1DDecoder busy-waits on dav1d EAGAIN — Audio/Video: Playback — S2/P2 NEW
- [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) — Crash in syscall | futex_wait (cubeb) — Audio/Video: cubeb — S2/P2 ASSIGNED
- [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) — 15% ve-av1-q wallclock regression on macOS (March 9) — Audio/Video: Playback — S2/P2 NEW
- [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) — [Meta] Bluetooth device related issues with audio and video — Audio/Video — S2/P2 NEW
- [2021379](https://bugzilla.mozilla.org/show_bug.cgi?id=2021379) — Crash in AsyncShutdownTimeout | CamerasParent — WebRTC: Audio/Video — S2/P2 NEW
- [2016455](https://bugzilla.mozilla.org/show_bug.cgi?id=2016455) — Crash in NS_CycleCollectorSuspect3 (RTCDataChannel::AnnounceClosed) — WebRTC — S2/P2 NEW
- [2023515](https://bugzilla.mozilla.org/show_bug.cgi?id=2023515) — Crash in libart.so / jni::Method (Android) — Audio/Video: Playback — S2/P2 NEW
- [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) — Crash in AudioDecoderInputTrack::EnsureTimeStretcher — Audio/Video — S2/P2 ASSIGNED
- [2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568) — Use a single rlbox sandbox for all soundtouch instances — Audio/Video: Playback — S2/P2 NEW
- [2020502](https://bugzilla.mozilla.org/show_bug.cgi?id=2020502) — NS_ERROR_DOM_MEDIA_DEMUXER_ERR in last 2 seconds of video — Audio/Video: Playback — S3/P2 NEW
- [2018955](https://bugzilla.mozilla.org/show_bug.cgi?id=2018955) — WebRTC playout fails silently at 768 kHz on macOS — WebRTC: Audio/Video — S3/P2 NEW
- [2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567) — Handle more TimeUnit overflow cases in MSE — Audio/Video: Playback — S3/P2 NEW
- [2023103](https://bugzilla.mozilla.org/show_bug.cgi?id=2023103) — Crash in abort | BuildFormat — WebRTC: Audio/Video — S3/P2 ASSIGNED
- [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) — x.com opens audio interface (PipeWire) despite nothing being played — Web Audio — S3/P2 NEW
- [2001005](https://bugzilla.mozilla.org/show_bug.cgi?id=2001005) — assertion "auth->password.len" failed (WebRTC: Networking) — S3/P3 NEW

**P3 and below (selected)**
- [2015946](https://bugzilla.mozilla.org/show_bug.cgi?id=2015946) — Google Meet crashes because WebRTC destroys a connected PipeWire stream — WebRTC — S2/-- ASSIGNED
- [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) — [meta] Media Related Sleep Issues — Audio/Video — S3/P3 NEW
- [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) — [meta] Interop 2025 Script Transform wpt.fyi timeout issues — WebRTC — S3/P3 NEW
- [2017189](https://bugzilla.mozilla.org/show_bug.cgi?id=2017189) — AV1 WebRTC decoding hangs almost instantly when streaming — WebRTC: Audio/Video — S3/P3 NEW
- [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) — Nvidia Tegra Video HW Decoding Regression with Firefox 142+ — S3/P3 NEW
- [2008617](https://bugzilla.mozilla.org/show_bug.cgi?id=2008617) — 4K AV1 Video decode doesn't work on YouTube — Audio/Video: Playback — S3/P3 UNCONFIRMED
- [2007762](https://bugzilla.mozilla.org/show_bug.cgi?id=2007762) — Audio/video desync when toggling speed on YouTube (PipeWire) — Audio/Video: cubeb — S3/P3 NEW
- [2013720](https://bugzilla.mozilla.org/show_bug.cgi?id=2013720) — Screen saver activates when streaming video on Linux Mint — Audio/Video: Playback — S3/P3 UNCONFIRMED
- [1973534](https://bugzilla.mozilla.org/show_bug.cgi?id=1973534) — HDMI audio cuts off after 1-2 seconds on Windows 11 AMD — Audio/Video: cubeb — S3/P3 ASSIGNED
- [2022422](https://bugzilla.mozilla.org/show_bug.cgi?id=2022422) — Origin Spoofing in WebRTCParent/Child unused PeerConnectionBlocker — WebRTC — S3/P3 NEW
- [1997480](https://bugzilla.mozilla.org/show_bug.cgi?id=1997480) — Crash in moz_wasm2c_memgrow_failed — Audio/Video — S3/P3 NEW
- [2023447](https://bugzilla.mozilla.org/show_bug.cgi?id=2023447) — High power consumption when playing YouTube videos — Audio/Video: Playback — S3/P3 UNCONFIRMED
- [2009596](https://bugzilla.mozilla.org/show_bug.cgi?id=2009596) — Intel Iris Xe doesn't show HDR video (Windows) — Audio/Video: Playback — S3/P3 NEW
- [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317) — Move Cubeb processing to utility process (Windows) — Audio/Video — S3/-- ASSIGNED
- [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) — Rework AudioIPC initialization to avoid blocking parent main thread — Audio/Video: cubeb — ASSIGNED
- [1972665](https://bugzilla.mozilla.org/show_bug.cgi?id=1972665) — Audio dies when switching audio tracks (Widevine) — Audio/Video: GMP — S3/P3 UNCONFIRMED

### Monthly Breakdown

```
Dec 2025  ███ (3)
Jan 2026  ████████ (8)
Feb 2026  ████████████ (12)
Mar 2026  ████████████████████████████ (23)
```

Activity is rising steeply in March, with an unusual density of S2 bugs in the final two weeks.

---

## Themes

---

### Theme 1: RTCDataChannel and WebRTC Crash Cluster (High-Volume Crashes)

**User-facing impact:** Firefox crashes during or after WebRTC calls. Two independent crash signatures affect all platforms at meaningful volume. The RTCDataChannel use-after-free crash hits 261 events in 30 days across Windows, macOS, and Linux. The CamerasParent async shutdown crash hits 158 events across Windows, primarily at browser close or profile change.

#### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|--------|---------|----------|--------|--------------|-------------------|
| [2016455](https://bugzilla.mozilla.org/show_bug.cgi?id=2016455) | Crash in [NS_CycleCollectorSuspect3 \| nsCycleCollectingAutoRefCnt::decr] (RTCDataChannel::AnnounceClosed) | S2 | NEW | 2026-03-17 | [261](https://crashes.mozilla.org/signatures?q=signature%3A%22NS_CycleCollectorSuspect3%20%7C%20nsCycleCollectingAutoRefCnt%3A%3Adecr%22) |
| [2021379](https://bugzilla.mozilla.org/show_bug.cgi?id=2021379) | Crash in [AsyncShutdownTimeout \| profile-before-change \| CamerasParent] | S2 | NEW | 2026-03-17 | [158](https://crashes.mozilla.org/signatures?q=signature%3A%22AsyncShutdownTimeout%20%7C%20profile-before-change%20%7C%20CamerasParent%22) |
| [2023103](https://bugzilla.mozilla.org/show_bug.cgi?id=2023103) | Crash in [abort \| BuildFormat] (WebRTC: Audio/Video) | S3 | ASSIGNED | 2026-03-17 | [45](https://crashes.mozilla.org/signatures?q=signature%3A%22abort%20%7C%20BuildFormat%22) |
| [2015946](https://bugzilla.mozilla.org/show_bug.cgi?id=2015946) | Google Meet crashes because WebRTC tries to destroy a connected PipeWire stream | S2 | ASSIGNED | 2026-03-17 | — |

#### Timeline Narrative

Bug [2016455](https://bugzilla.mozilla.org/show_bug.cgi?id=2016455) was filed in mid-February 2026 and has sat in NEW with no assignee. The cycle collector crash signature affecting RTCDataChannel is generating 261 hits across all major platforms (Windows, macOS, Linux) and all release channels including nightly. This strongly suggests the root cause is in code present across all build configs and not a recent regression. Bug [2021379](https://bugzilla.mozilla.org/show_bug.cgi?id=2021379) was filed March 5 and the CamerasParent shutdown crash (158 hits, Windows-dominant) has 5 comments but no assignee. Bug [2023103](https://bugzilla.mozilla.org/show_bug.cgi?id=2023103) is ASSIGNED and actively being worked.

**Stagnation callout:** [2016455](https://bugzilla.mozilla.org/show_bug.cgi?id=2016455) is S2 with 261 crash events per 30 days, has been NEW since 2026-02-12 with a single comment and no assignee. This is a top-priority stagnation concern.

---

### Theme 2: Bluetooth Audio — Meta-Bug with 23+ Dependents (Systemic Platform Issue)

**User-facing impact:** Users with Bluetooth headphones, earbuds (AirPods, Pixel Buds, Galaxy Buds), and speakers experience a wide range of failures in Firefox: audio stuttering, desync, silence after reconnect, muting during video playback, and media pause/resume failures when disconnecting devices. The meta-bug [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) was created in January 2026 with 23 dependent bugs spanning years of reports.

#### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) | [Meta] Bluetooth device related issues with audio and video | S2 | NEW | 2026-03-18 |
| [1999582](https://bugzilla.mozilla.org/show_bug.cgi?id=1999582) | Short Bluetooth audio hiccup when reloading or closing another tab | S3 | UNCONFIRMED | 2026-03-14 |
| [1987257](https://bugzilla.mozilla.org/show_bug.cgi?id=1987257) | Audio on macOS 15 with AirPods Pro 2 desynchronized between earbuds | S3 | UNCONFIRMED | 2026-03-14 |
| [1957088](https://bugzilla.mozilla.org/show_bug.cgi?id=1957088) | sesame.com — can't hear AI on voice demo with bluetooth headphones | S3 | NEW | 2026-02-05 |
| [2020653](https://bugzilla.mozilla.org/show_bug.cgi?id=2020653) | Disconnecting AirPods no longer pauses media (YouTube) | S3 | UNCONFIRMED | 2026-03-14 |
| [1973353](https://bugzilla.mozilla.org/show_bug.cgi?id=1973353) | Delayed video start/resume by Bluetooth | S2 | UNCONFIRMED | 2026-03-11 |
| [2007835](https://bugzilla.mozilla.org/show_bug.cgi?id=2007835) | Audio stutters during video playback with Pixel Buds Pro 2 | S3 | UNCONFIRMED | 2026-01-21 |
| [2008968](https://bugzilla.mozilla.org/show_bug.cgi?id=2008968) | YouTube video stutters at start/seeking with Bluetooth output | S3 | UNCONFIRMED | 2026-01-21 |
| [2008781](https://bugzilla.mozilla.org/show_bug.cgi?id=2008781) | Bluetooth audio stuttering when playing a video | S3 | UNCONFIRMED | 2026-03-04 |
| [1936931](https://bugzilla.mozilla.org/show_bug.cgi?id=1936931) | Video desyncs with audio after YouTube ads with Bluetooth headphones | S3 | UNCONFIRMED | 2026-01-21 |
| [1937317](https://bugzilla.mozilla.org/show_bug.cgi?id=1937317) | All videos stop playing if headphones removed while playing | S3 | NEW | 2026-01-21 |
| [1888896](https://bugzilla.mozilla.org/show_bug.cgi?id=1888896) | Bluetooth headset A2DP vs. HFP switching audio issue (Windows) | S3 | NEW | 2026-01-21 |
| [1678846](https://bugzilla.mozilla.org/show_bug.cgi?id=1678846) | No sound after disconnect/reconnect Bluetooth speaker | S3 | NEW | 2026-03-15 |
| [2021805](https://bugzilla.mozilla.org/show_bug.cgi?id=2021805) | Firefox mutes YouTube video for a second on Wheel-Click in tweet | S3 | UNCONFIRMED | 2026-03-17 |

#### Timeline Narrative

The meta-bug was organized in January 2026, consolidating reports dating back to 2018. Nearly all child bugs remain UNCONFIRMED or NEW with no assignee. The meta-bug itself has only 1 comment. The most recent child bugs — filed in late 2025 and early 2026 — show the problem is still actively being hit by users across all platforms. Bug [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) (cubeb futex crash, Linux, 51 Socorro hits) and bug [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) (AudioIPC initialization rework to unblock parent main thread) are being actively developed and appear related to the broader cubeb/audio device management picture.

**Stagnation callout:** The meta-bug [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) is S2/P2 with 23 dependents filed over 7+ years. No active development is visible against the top-level meta, only incremental filing of new child bugs.

---

### Theme 3: Cubeb Linux Crash and AudioIPC Jank (Active Development)

**User-facing impact:** On Linux, Firefox crashes in the audio subsystem via a futex syscall in cubeb. Separately, audio initialization blocks the parent process main thread on Windows, causing multi-second jank. Both issues are being worked.

#### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|--------|---------|----------|--------|--------------|-------------------|
| [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) | Crash in [syscall \| std::sys::pal::unix::futex::futex_wait] | S2 | ASSIGNED | 2026-03-18 | [51](https://crashes.mozilla.org/signatures?q=signature%3A%22syscall%20%7C%20std%3A%3Asys%3A%3Apal%3A%3Aunix%3A%3Afutex%3A%3Afutex_wait%22) |
| [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) | Rework AudioIPC initialization to avoid blocking parent main thread | — | ASSIGNED | 2026-03-19 | — |
| [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317) | Move Cubeb processing to a utility process (Windows) | S3 | ASSIGNED | 2026-03-18 | — |
| [1903051](https://bugzilla.mozilla.org/show_bug.cgi?id=1903051) | Massive parent process jank when hovering video in Google Drive | S3 | NEW | 2026-03-18 | — |
| [1956979](https://bugzilla.mozilla.org/show_bug.cgi?id=1956979) | 9s jank trying to run PContent::Msg_CreateAudioIPCConnection (win10) | S3 | ASSIGNED | 2025-04-01 | — |
| [2007762](https://bugzilla.mozilla.org/show_bug.cgi?id=2007762) | Audio/video desync when toggling speed on YouTube (PipeWire) | S3 | NEW | 2026-03-15 | — |
| [1973534](https://bugzilla.mozilla.org/show_bug.cgi?id=1973534) | HDMI audio cuts off after 1-2 seconds on Windows 11 AMD | S3 | ASSIGNED | 2026-03-18 | — |

#### Timeline Narrative

Bug [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) (futex crash, 51 Linux hits) and [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) (AudioIPC rework) were filed on the same day (2026-03-12 and 2026-03-18 respectively) and are linked in the dependency graph — [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) blocks both [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) and [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317), indicating coordinated work. The utility process migration ([1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317)) is the long-term solution to both the jank and crash vectors.

---

### Theme 4: Media Sleep/Wake Handling — Meta-Bug with 16 Dependents

**User-facing impact:** After a computer enters sleep mode and wakes, Firefox frequently fails to resume audio or video correctly: audio may go silent while video continues, the display may go to sleep during active video playback, the screen saver activates, or media unexpectedly resumes on the Windows lock screen.

#### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) | [meta] Media Related Sleep Issues | S3 | NEW | 2026-03-15 |
| [1519935](https://bugzilla.mozilla.org/show_bug.cgi?id=1519935) | Windows Sleep mode causes video to stop after waking | S3 | NEW | 2026-03-15 |
| [1821102](https://bugzilla.mozilla.org/show_bug.cgi?id=1821102) | Firefox keeps coreaudiod active, preventing sleep on macOS | S3 | UNCONFIRMED | 2026-03-15 |
| [1606331](https://bugzilla.mozilla.org/show_bug.cgi?id=1606331) | Netflix video continues after sleep but sound stops | S3 | NEW | 2026-03-15 |
| [1869101](https://bugzilla.mozilla.org/show_bug.cgi?id=1869101) | After sleep, video is slow and choppy (not Edge) | S3 | UNCONFIRMED | 2026-03-15 |
| [1977132](https://bugzilla.mozilla.org/show_bug.cgi?id=1977132) | Media resumes on Windows lock screen after waking from sleep | S3 | NEW | 2026-03-15 |
| [1984927](https://bugzilla.mozilla.org/show_bug.cgi?id=1984927) | Display goes to sleep while watching YouTube | S3 | NEW | 2026-03-14 |
| [2013720](https://bugzilla.mozilla.org/show_bug.cgi?id=2013720) | Screen saver activates when streaming video in Firefox on Linux Mint | S3 | UNCONFIRMED | 2026-03-16 |
| [1913428](https://bugzilla.mozilla.org/show_bug.cgi?id=1913428) | End of video in fullscreen doesn't trigger system sleep timer | S3 | UNCONFIRMED | 2026-03-15 |
| [1961596](https://bugzilla.mozilla.org/show_bug.cgi?id=1961596) | Unmuted video doesn't play after computer sleep on macOS | S3 | UNCONFIRMED | 2026-03-15 |
| [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) | x.com opens audio interface (PipeWire) despite nothing playing | S3 | NEW | 2026-03-18 |
| [1959613](https://bugzilla.mozilla.org/show_bug.cgi?id=1959613) | Audio stream remains open when playback paused | S4 | UNCONFIRMED | 2026-03-18 |

#### Timeline Narrative

The meta-bug [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) was created 2026-03-14 to consolidate reports going back to 2019. All dependent bugs received an update timestamp at 2026-03-15, indicating the filing/triage sweep was thorough. The related bug [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) (x.com waking audio on PipeWire) is linked to [2002450](https://bugzilla.mozilla.org/show_bug.cgi?id=2002450) which aims to remove the AudioDestinationNode track when idle — an active fix. The sleep/wake category overlaps heavily with the Bluetooth theme because both involve hardware device state transitions.

---

### Theme 5: AV1 Decode Failures and Regressions

**User-facing impact:** AV1 video decode is failing or regressing in multiple distinct ways: high-bitrate streams freeze in dav1d (busy-wait bug), 4K YouTube decode fails outright on some hardware, a 15% performance regression appeared on macOS in early March, WebRTC AV1 streaming hangs immediately, and an FFmpegVideoDecoder stats overflow crash is actively being fixed.

#### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) | High-bitrate AV1 freezes: DAV1DDecoder busy-waits on EAGAIN | S2 | NEW | 2026-03-18 |
| [2024007](https://bugzilla.mozilla.org/show_bug.cgi?id=2024007) | AssertedCast int64_t→float overflow in FFmpegVideoDecoder::DecodeStats | S2/P1 | ASSIGNED | 2026-03-19 |
| [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) | 15% ve-av1-q wallclock regression on macOS (March 9 2026) | S2 | NEW | 2026-03-18 |
| [2008617](https://bugzilla.mozilla.org/show_bug.cgi?id=2008617) | 4K AV1 Video decode doesn't work on YouTube | S3 | UNCONFIRMED | 2026-03-19 |
| [2017189](https://bugzilla.mozilla.org/show_bug.cgi?id=2017189) | AV1 WebRTC decoding hangs almost instantly when streaming | S3 | NEW | 2026-03-16 |
| [2020502](https://bugzilla.mozilla.org/show_bug.cgi?id=2020502) | NS_ERROR_DOM_MEDIA_DEMUXER_ERR in last 2 seconds of video | S3 | NEW | 2026-03-19 |
| [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) | Nvidia Tegra Video HW Decoding Regression with Firefox 142+ | S3 | NEW | 2026-03-15 |

#### Timeline Narrative

The AV1 cluster has grown significantly in February-March 2026. Bug [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) was filed Feb 12 and has accumulated 5 comments, with the busy-wait behavior in `DAV1DDecoder::InvokeDecode` well-described but still open. Bug [2024007](https://bugzilla.mozilla.org/show_bug.cgi?id=2024007) was filed March 17 and is already ASSIGNED/P1 — the fuzzer caught an integer cast overflow in the FFmpeg stats path. Bug [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) is a performance regression (perf-alert) tied to a specific March 9 commit window. Bug [2017189](https://bugzilla.mozilla.org/show_bug.cgi?id=2017189) (WebRTC AV1 hang, 23 comments) is the most commented and has been building user attention since February.

**Stagnation callout:** [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) is S2/P2 with a clear root-cause description and no assignee after 35 days.

---

### Theme 6: WebRTC RTCRtpScriptTransform / Encoded Transform Reliability (Interop 2025)

**User-facing impact:** RTCRtpScriptTransform (Encoded Transform) test cases on wpt.fyi time out intermittently in Firefox. This affects Interop 2025 scoring and potentially real-world insertable streams applications.

#### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) | [meta] Interop 2025 Script Transform wpt.fyi timeout issues | S3 | NEW | 2026-03-17 |
| [2010655](https://bugzilla.mozilla.org/show_bug.cgi?id=2010655) | script-metadata-transform.https.html times out (>60s) on wpt.fyi | S3 | NEW | 2026-03-17 |
| [2010661](https://bugzilla.mozilla.org/show_bug.cgi?id=2010661) | script-change-transform.https.html times out on wpt.fyi | S3 | NEW | 2026-03-17 |
| [2010663](https://bugzilla.mozilla.org/show_bug.cgi?id=2010663) | script-write-twice-transform.https.html times out on wpt.fyi | S3 | NEW | 2026-03-17 |
| [2010667](https://bugzilla.mozilla.org/show_bug.cgi?id=2010667) | RTCRtpScriptTransform-encoded-transform.https.html times out (>60s) | S3 | NEW | 2026-03-17 |
| [2005780](https://bugzilla.mozilla.org/show_bug.cgi?id=2005780) | script-transform-generateKeyFrame-simulcast unreliable on Windows | S3 | NEW | 2026-03-17 |

#### Timeline Narrative

All five individual timeout bugs were filed 2026-01-15 and the meta-bug was filed 2026-03-17. The child bugs range from P2 to P3. Bug [2010657](https://bugzilla.mozilla.org/show_bug.cgi?id=2010657) (one of the six dependents) is already RESOLVED. These are intermittent-but-reproducible on wpt.fyi, which runs Firefox builds on continuous infrastructure. The core issue appears to be a race condition or timing sensitivity in the ScriptTransform ReadableStream pipeline under load.

---

### Theme 7: GMP / Widevine / AppLocker Security and Reliability

**User-facing impact:** The GMP plugin loading mechanism fails under enterprise AppLocker policies that use Publisher rules with restricted token levels, breaking Widevine DRM content for enterprise users. Separately, audio dies when switching Widevine audio tracks.

#### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) | AppLocker Publisher rules don't work with USER_RESTRICTED token | S3/P1 | ASSIGNED | 2026-03-17 |
| [1830431](https://bugzilla.mozilla.org/show_bug.cgi?id=1830431) | Crash in mozilla::gmp::GMPLoader::Load | S3 | NEW | 2026-03-13 |
| [1972665](https://bugzilla.mozilla.org/show_bug.cgi?id=1972665) | Audio dies when switching audio tracks (Widevine, Desktop only) | S3 | UNCONFIRMED | 2026-03-18 |
| [2023254](https://bugzilla.mozilla.org/show_bug.cgi?id=2023254) | Fix lifetimes for RemoteMediaDataEncoderChild and RemoteCDMChild | S3 | ASSIGNED | 2026-03-15 |

#### Timeline Narrative

Bug [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) is P1 and actively being worked; it blocks [1830431](https://bugzilla.mozilla.org/show_bug.cgi?id=1830431). The AppLocker issue is enterprise-relevant. Bug [2023254](https://bugzilla.mozilla.org/show_bug.cgi?id=2023254) addresses IPC lifetime correctness for CDM/encoder children, which has safety implications for the media utility process architecture.

---

### Theme 8: Web Audio Idle Resource Leak and Privacy (Emerging)

**User-facing impact:** Web Audio opens and holds audio device resources (PipeWire streams on Linux) even when no audio is being played, wasting battery and potentially leaking device activity indicators. Separately, audio device names in `about:support` may expose personally identifiable information.

#### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|--------------|
| [2023970](https://bugzilla.mozilla.org/show_bug.cgi?id=2023970) | about:support can leak PII via audio device names | S2 | NEW | 2026-03-19 |
| [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) | x.com opens audio interface (PipeWire) despite nothing playing | S3 | NEW | 2026-03-18 |
| [1959613](https://bugzilla.mozilla.org/show_bug.cgi?id=1959613) | Audio stream remains open when playback paused | S4 | UNCONFIRMED | 2026-03-18 |
| [2002450](https://bugzilla.mozilla.org/show_bug.cgi?id=2002450) | Remove AudioDestinationNode audio output when idle | — | ASSIGNED | 2026-03-18 |

#### Timeline Narrative

Bug [2023970](https://bugzilla.mozilla.org/show_bug.cgi?id=2023970) was filed on 2026-03-17 and reached S2/P2 very quickly. Exposing audio device names in `about:support` is not new behavior but the privacy framing is a recent escalation. Bug [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) is directly connected to [2002450](https://bugzilla.mozilla.org/show_bug.cgi?id=2002450) which is being fixed. The idle audio stream problem is the root cause behind both spurious device wakeups and the sleep prevention reports in Theme 4.

---

### Theme 9: EnsureTimeStretcher Crash and Soundtouch rlbox (Active Safety Work)

**User-facing impact:** Firefox crashes in `AudioDecoderInputTrack::EnsureTimeStretcher` during media playback on Windows, particularly when using playback speed control. A related refactor to use a single rlbox sandbox for all soundtouch instances is being developed.

#### Breadcrumb Table

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|--------|---------|----------|--------|--------------|-------------------|
| [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) | Crash in [mozilla::AudioDecoderInputTrack::EnsureTimeStretcher] | S2 | ASSIGNED | 2026-03-16 | [21](https://crashes.mozilla.org/signatures?q=signature%3A%22mozilla%3A%3AAudioDecoderInputTrack%3A%3AEnsureTimeStretcher%22) |
| [2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568) | Use a single rlbox sandbox for all soundtouch instances | S2 | NEW | 2026-03-17 | — |

#### Timeline Narrative

Bug [2011539](https://bugzilla.mozilla.org/show_bug.cgi?id=2011539) was filed 2026-01-20 and is ASSIGNED with 6 comments. The `topcrash` keyword indicates it has been recognized in the crash dashboard. It hits Windows across release, beta, and ESR. The soundtouch rlbox consolidation ([2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568)) may fix the crash by changing sandbox lifetime semantics.

---

## Closing

### Ranked Signal Summary

| Rank | Theme | Breadcrumb Count | Meta-Bug | Top Severity | Notes |
|------|-------|-----------------|----------|-------------|-------|
| 1 | RTCDataChannel / CamerasParent Crash Cluster | 4 | No | S2 | 261 + 158 + 45 crash hits; S2 NEW stagnant 35d |
| 2 | Bluetooth Audio — Systemic Platform Failures | 23+ | [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) | S2 | Meta is S2/P2, 23 deps, no active dev |
| 3 | AV1 Decode Failures and Regressions | 7 | No | S2/P1 | 4 distinct failure modes; P1 being worked |
| 4 | Media Sleep/Wake Handling | 16+ | [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) | S3 | Meta created March 2026; all platforms |
| 5 | Cubeb Linux Crash / AudioIPC Jank | 7 | No | S2 | 51 Linux crash hits; active fix in progress |
| 6 | EnsureTimeStretcher Crash / Soundtouch rlbox | 2 | No | S2/topcrash | 21 Windows hits; assigned + coordinated fix |
| 7 | WebRTC Script Transform Reliability (Interop 2025) | 6 | [2023893](https://bugzilla.mozilla.org/show_bug.cgi?id=2023893) | S3 | Affects Interop 2025 scoring; no assignee |
| 8 | GMP / AppLocker / Widevine | 4 | No | S3/P1 | Enterprise-relevant; being worked |
| 9 | Web Audio Idle Resource Leak and Privacy | 4 | No | S2 | PII report escalated; root-cause fix in progress |

### Resources Used

- Bugzilla REST API (WebFetch)
- Socorro crash analysis (`socorro-cli`)
- Searchfox (not needed for this run)

### Suggestions for Improving This Skill

- The `--date` window filter for `socorro-cli` did not return count-only output in the AGGREGATIONS block; the trend comparison relied on the FOUND count from the first lines. A dedicated count mode or structured JSON output from `socorro-cli` would make 30d/60d trend comparison more reliable.
- The Bugzilla REST API does not return `cc_count` when `include_fields` is specified alongside it. Augmenting seed enrichment with a secondary per-bug fetch for cc_count would allow more accurate signal scoring for the community-interest dimension.
- Adding a `assignee` field to the include_fields list would avoid the need to infer stagnation purely from last_change_time; it would allow direct detection of unassigned S1/S2 bugs.

---

"Every great discovery begins not with an answer, but with someone refusing to stop asking questions." — Anonymous
