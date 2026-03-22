# Bugzilla Wrangler Report — Media
**Generated:** 2026-03-22

---

## Session Info

| Field | Value |
|---|---|
| **Scope profile** | `media` — Core: Audio/Video, Audio/Video: cubeb, Audio/Video: GMP, Audio/Video: MediaStreamGraph, Audio/Video: Playback, Audio/Video: Recording, Audio/Video: Web Codecs, Web Audio |
| **Seed timeframe** | 2025-10-01 → 2026-03-20 |
| **Seed count** | 46 |
| **Seed mode** | mixed-seed (29 created + 17 changed = 46 unique) |
| **Cache freshness** | Fetched live — existing cache file was from a prior session |
| **Socorro enrichment** | Completed via SuperSearch API |

---

## Seed Info

### Seed Bugs by Priority

**P1**
- [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) — AppLocker Publisher rules don't work when loading DLLs with USER_RESTRICTED token level (GMP, S3) — *Assigned: bobowen*

**P2**
- [2023515](https://bugzilla.mozilla.org/show_bug.cgi?id=2023515) — Crash in `libc.so | <.plt ELF section in libmozglue.so> | libart.so` (Playback, S2, topcrash) — *Assigned: jhlin*
- [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) — Crash in `syscall | std::sys::pal::unix::futex::futex_wait` (cubeb, S2) — *Assigned: kinetik*
- [2023970](https://bugzilla.mozilla.org/show_bug.cgi?id=2023970) — about:support can leak PII via audio device names (Web Audio, S2)
- [2023568](https://bugzilla.mozilla.org/show_bug.cgi?id=2023568) — Use a single rlbox sandbox for all soundtouch instances (Playback, S2)
- [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) — High-bitrate AV1 freezes: DAV1DDecoder busy-waits on dav1d EAGAIN (Playback, S2)
- [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) — [Meta] Bluetooth device related issues with audio and video (AV, S2) — *Assigned: kinetik*
- [2024598](https://bugzilla.mozilla.org/show_bug.cgi?id=2024598) — Crash in `mozilla::AudioCallbackDriver::OutputChannelCount` (AV, S3)
- [2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567) — Handle more TimeUnit overflow cases in MSE (Playback, S3) — *Assigned: padenot*
- [1992579](https://bugzilla.mozilla.org/show_bug.cgi?id=1992579) — Memory leak with F1TV (Playback, S3)
- [2021179](https://bugzilla.mozilla.org/show_bug.cgi?id=2021179) — Instagram reels audio static/mute after scrolling (cubeb, S3)
- [1916629](https://bugzilla.mozilla.org/show_bug.cgi?id=1916629) — Crash in `mio::sys::windows::named_pipe::read_done` (Playback, S3, topcrash) — *Assigned: kinetik*
- [1984064](https://bugzilla.mozilla.org/show_bug.cgi?id=1984064) — Android 14 emulator media failures on debug (AV, S2) — *Assigned: kinetik*
- [1978703](https://bugzilla.mozilla.org/show_bug.cgi?id=1978703) — AV1 video stuttering with media.ffvpx-hw.enabled (Playback, S3, REOPENED)
- [1962665](https://bugzilla.mozilla.org/show_bug.cgi?id=1962665) — Firefox and PlayReady: video black, audio ok (Playback, S3)
- [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) — x.com causes audio interface to be opened (PipeWire) (Web Audio, S3)
- [1999168](https://bugzilla.mozilla.org/show_bug.cgi?id=1999168) — VideoDecoder.isConfigSupported() returns false for HEVC hev1 (Web Codecs, S3)

**P3**
- [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) — AV1-q perf regression macOS Mar 9 2026 (Playback, S3)
- [2021122](https://bugzilla.mozilla.org/show_bug.cgi?id=2021122) — HEVC video doesn't play in flatpak builds (Playback, S3)
- [2023367](https://bugzilla.mozilla.org/show_bug.cgi?id=2023367) — Videos not playing (AV, S3)
- [2023823](https://bugzilla.mozilla.org/show_bug.cgi?id=2023823) — MSE audio track desyncs from video on loop seek (Playback, S3)
- [2023594](https://bugzilla.mozilla.org/show_bug.cgi?id=2023594) — Applying a rotation to a video causes colors to shift (Web Codecs, S3, regression)
- [2024183](https://bugzilla.mozilla.org/show_bug.cgi?id=2024183) — Don't allocate time stretcher on the audio thread (MediaStreamGraph, S3)
- [2008617](https://bugzilla.mozilla.org/show_bug.cgi?id=2008617) — 4K AV1 video decode doesn't work on YouTube (Playback, S3)
- [2021805](https://bugzilla.mozilla.org/show_bug.cgi?id=2021805) — Firefox mutes YouTube for a second on wheel-click a Tweet (Playback, S3)
- [2023447](https://bugzilla.mozilla.org/show_bug.cgi?id=2023447) — High power consumption and heat when playing YouTube videos (Playback, S3)
- [2013720](https://bugzilla.mozilla.org/show_bug.cgi?id=2013720) — Screen saver activates during video streaming on Linux Mint (Playback, S3)
- [2009596](https://bugzilla.mozilla.org/show_bug.cgi?id=2009596) — [HDR/Windows] Intel Iris Xe doesn't show HDR video (Playback, S3)
- [1997480](https://bugzilla.mozilla.org/show_bug.cgi?id=1997480) — Crash in `moz_wasm2c_memgrow_failed` (AV, S3)
- [1997802](https://bugzilla.mozilla.org/show_bug.cgi?id=1997802) — Play/Pause media key does nothing while video is playing (Playback, S3)
- [1999639](https://bugzilla.mozilla.org/show_bug.cgi?id=1999639) — Rapid audio playback causes audiodg to use multiple GB of RAM on Windows (cubeb, S3)
- [2002910](https://bugzilla.mozilla.org/show_bug.cgi?id=2002910) — Replace user interaction with explicit control for video playback (Playback, S3)
- [1941471](https://bugzilla.mozilla.org/show_bug.cgi?id=1541471) — [Meta] Implement spec-compliant HTMLMediaElement.captureStream (MediaStreamGraph, S3) — *Assigned: alwu*
- [1973534](https://bugzilla.mozilla.org/show_bug.cgi?id=1973534) — HDMI audio cuts off after 1-2s, AMD HD Audio, Windows 11 (cubeb, S3) — *Assigned: kinetik*
- [1972665](https://bugzilla.mozilla.org/show_bug.cgi?id=1972665) — Audio dies when switching audio tracks (Widevine, Desktop) (GMP, S3)
- [1987266](https://bugzilla.mozilla.org/show_bug.cgi?id=1987266) — Tabs freeze and crash on background play on secondary screen (Playback, S3)
- [1984763](https://bugzilla.mozilla.org/show_bug.cgi?id=1984763) — MOZ_CRASH MozPromise ThenValue destroyed without being disconnected (Playback, S3)
- [1942421](https://bugzilla.mozilla.org/show_bug.cgi?id=1942421) — Enable H265 Decoder on Windows for WebCodecs (Web Codecs, S3)
- [1986315](https://bugzilla.mozilla.org/show_bug.cgi?id=1986315) — AAC in MP4, channel index 7 (7.1) rendered incorrectly (AV, S3) — *Assigned: padenot*
- [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317) — Move Cubeb processing to a utility process (Windows) (AV) — *Assigned: kinetik*
- [1903051](https://bugzilla.mozilla.org/show_bug.cgi?id=1903051) — Massive parent process jank when hovering over video in Google Drive (cubeb, S3)
- [1997237](https://bugzilla.mozilla.org/show_bug.cgi?id=1997237) — YouTube won't play in private window after browsing yahoo.com (Playback, S3)
- [1978703](https://bugzilla.mozilla.org/show_bug.cgi?id=1978703) (listed under P2 above)

**P4/P5 (older, low-priority bugs active in window)**
- [2024618](https://bugzilla.mozilla.org/show_bug.cgi?id=2024618) — Make MediaData::As() use a release assert (AV, S3, sec-want)
- [1716249](https://bugzilla.mozilla.org/show_bug.cgi?id=1716249) — Selecting default input device - ALSA/Linux (cubeb, S4)
- [1650131](https://bugzilla.mozilla.org/show_bug.cgi?id=1650131) — Microphone doesn't work on Linux ALSA (cubeb, S4)
- [1959613](https://bugzilla.mozilla.org/show_bug.cgi?id=1959613) — Audio stream remains open when playback paused (cubeb, S4)

### Creation Date Timeline

Breakdown of seed bugs **created within the window** (Query A = 29 bugs; all Query B seeds were created before Oct 2025 and captured only because of recent activity):

```
Oct 2025  ████  (3)
Nov 2025  █████ (4)
Dec 2025  ·     (0) — all Dec bugs had intermittent-failure keyword; filtered
Jan 2026  █████ (4)
Feb 2026  ██    (2)
Mar 2026  ████████████████ (16)
          ──────────────────────────────────────────────
          Oct  Nov  Dec  Jan  Feb  Mar
```

> **Note:** December coverage gap is due to intermittent-failure filtering. The March spike reflects high recent bug-filing activity, not a data artifact.

---

## Themes

---

### Theme 1 — Bluetooth Audio Disruption (Multi-Platform)

**User impact:** Users experience audio stutter, desync between left/right earbuds, complete audio cutoff, or browser muting media when interacting with Bluetooth headphones or speakers. Disconnecting a BT device can cause video to stop playing entirely or fail to rebind to the new output.

| Bug ID | Summary | Severity | Status | Last Changed |
|---|---|---|---|---|
| [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) | [Meta] Bluetooth device related issues — *Assigned: kinetik* | S2 | NEW | 2026-03-20 |
| [1492488](https://bugzilla.mozilla.org/show_bug.cgi?id=1492488) | Can't get audio to work over BT with Bluetooth headset (Windows) | S3 | NEW | 2026-01-21 |
| [1706131](https://bugzilla.mozilla.org/show_bug.cgi?id=1706131) | Popping/crackling sounds in BT fast-forward mode | S3 | NEW | 2026-01-21 |
| [1824617](https://bugzilla.mozilla.org/show_bug.cgi?id=1824617) | Audio stuttering while using Bluetooth headphones | S3 | UNCONFIRMED | 2026-01-21 |
| [1835986](https://bugzilla.mozilla.org/show_bug.cgi?id=1835986) | Audio and video stutter with Bluetooth output (Android 13) | S3 | NEW | 2026-01-21 |
| [1856251](https://bugzilla.mozilla.org/show_bug.cgi?id=1856251) | Bluetooth audio immediately goes silent on vidplay/mycloud | S3 | UNCONFIRMED | 2026-01-21 |
| [1861456](https://bugzilla.mozilla.org/show_bug.cgi?id=1861456) | Joining call with BT headphones causes audio failure (Pixel 3XL) — *Assigned: padenot* | S3 | NEW | 2026-01-21 |
| [1868267](https://bugzilla.mozilla.org/show_bug.cgi?id=1868267) | Desynched audio channels with BT AirPods on play/pause | S3 | UNCONFIRMED | 2026-01-21 |
| [1888896](https://bugzilla.mozilla.org/show_bug.cgi?id=1888896) | Bluetooth A2DP / HSP+HFP switching issue on Windows — *Assigned: padenot* | S3 | NEW | 2026-01-21 |
| [1936931](https://bugzilla.mozilla.org/show_bug.cgi?id=1936931) | Video desyncs with audio after YouTube ads with BT headphones | S3 | UNCONFIRMED | 2026-01-21 |
| [1937317](https://bugzilla.mozilla.org/show_bug.cgi?id=1937317) | All videos stop playing if headphones removed while playing (regression) — *Assigned: kinetik* | S3 | NEW | 2026-01-21 |
| [1939288](https://bugzilla.mozilla.org/show_bug.cgi?id=1939288) | Turning off BT headphones causes video to stutter/pause | — | UNCONFIRMED | 2026-01-21 |
| [1957088](https://bugzilla.mozilla.org/show_bug.cgi?id=1957088) | sesame.com — can't hear AI voice demo with BT headphones | S3 | NEW | 2026-02-05 |
| [1961555](https://bugzilla.mozilla.org/show_bug.cgi?id=1961555) | Pixel Buds A-Series stutter during YouTube autoplay (Android) | S3 | UNCONFIRMED | 2026-01-21 |
| [1973353](https://bugzilla.mozilla.org/show_bug.cgi?id=1973353) | Delayed video start/resume with Bluetooth | S3 | UNCONFIRMED | 2026-03-20 |
| [1987257](https://bugzilla.mozilla.org/show_bug.cgi?id=1987257) | AirPods Pro 2 left/right desync on macOS 15 | S3 | UNCONFIRMED | 2026-03-14 |
| [1990361](https://bugzilla.mozilla.org/show_bug.cgi?id=1990361) | Audio cut when using Bluetooth headset | S3 | NEW | 2026-01-21 |
| [1999582](https://bugzilla.mozilla.org/show_bug.cgi?id=1999582) | Short BT audio hiccup on tab reload/close | S3 | UNCONFIRMED | 2026-03-14 |
| [2007835](https://bugzilla.mozilla.org/show_bug.cgi?id=2007835) | Audio stutters with Pixel Buds Pro 2 during video | S3 | UNCONFIRMED | 2026-01-21 |
| [2008781](https://bugzilla.mozilla.org/show_bug.cgi?id=2008781) | Bluetooth audio stuttering during video | S3 | UNCONFIRMED | 2026-03-04 |
| [2008968](https://bugzilla.mozilla.org/show_bug.cgi?id=2008968) | YouTube stutters at start/seek with BT output | S3 | UNCONFIRMED | 2026-01-21 |
| [2009171](https://bugzilla.mozilla.org/show_bug.cgi?id=2009171) | Intermittent freeze after BT disconnect (Windows 11) | S3 | UNCONFIRMED | 2026-03-05 |
| [2020653](https://bugzilla.mozilla.org/show_bug.cgi?id=2020653) | Disconnecting AirPods no longer pauses media in YouTube | S3 | UNCONFIRMED | 2026-03-14 |
| [2021805](https://bugzilla.mozilla.org/show_bug.cgi?id=2021805) | Firefox mutes YouTube for a second on wheel-click a Tweet | S3 | UNCONFIRMED | 2026-03-17 |
| [1678846](https://bugzilla.mozilla.org/show_bug.cgi?id=1678846) | No sound after Bluetooth speaker disconnect/reconnect (regression) — *Assigned: padenot* | S3 | NEW | 2026-03-15 |

**Timeline:** Reports span from 2018 (bug 1492488) to March 2026, with accelerating volume since late 2024. The meta bug 2011679 was created 2026-01-21 and is assigned to Matthew Gregan [:kinetik] as the triage point. 23 independent child bugs cover Windows, macOS, Android, and Linux, across all BT profile types (A2DP, HFP, HSP). New reports continue to arrive; 2020653 and 2021805 were filed in March 2026.

**Signal:** Very high. Meta bug with 23+ child reports from independent reporters across platforms. S2/P2 meta. Active assignee. Multiple padenot-assigned sub-bugs. No single root fix yet.

---

### Theme 2 — Windows Named Pipe / AudioIPC Crash Storm

**User impact:** Firefox crashes silently in the content process on Windows when audio is active. This is a top crash traced to the `mio` library's Windows named pipe implementation used by the AudioIPC subsystem. A parallel crash (futex hang) affects Linux users.

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|---|---|---|---|---|---|
| [1916629](https://bugzilla.mozilla.org/show_bug.cgi?id=1916629) | Crash in `mio::sys::windows::named_pipe::read_done` — *Assigned: kinetik* | S3 | ASSIGNED | 2026-03-19 | **3,917** |
| [2024485](https://bugzilla.mozilla.org/show_bug.cgi?id=2024485) | Update mio to 1.1.1 (fix) — *Assigned: kinetik* | — | RESOLVED | 2026-03-19 | — |
| [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) | Crash in `syscall | std::sys::pal::unix::futex::futex_wait` — *Assigned: kinetik* | S2 | ASSIGNED | 2026-03-18 | **182** |
| [2024498](https://bugzilla.mozilla.org/show_bug.cgi?id=2024498) | Rework AudioIPC initialization to avoid blocking parent main thread — *Assigned: kinetik* | — | ASSIGNED | 2026-03-19 | — |
| [1899317](https://bugzilla.mozilla.org/show_bug.cgi?id=1899317) | Move Cubeb processing to a utility process (Windows) — *Assigned: kinetik* | — | ASSIGNED | 2026-03-18 | — |
| [2024598](https://bugzilla.mozilla.org/show_bug.cgi?id=2024598) | Crash in `mozilla::AudioCallbackDriver::OutputChannelCount` | S3 | NEW | 2026-03-19 | 1 |

**Crash Details — [mio::sys::windows::named_pipe::read_done](https://crashes.mozilla.org/signatures?q=signature%3A%22mio%3A%3Asys%3A%3Awindows%3A%3Anamed_pipe%3A%3Aread_done%22):**
- 7-day: **904** | 30-day: **3,917** crashes
- Platform: Windows NT (100%)
- Channels: ESR ~56%, Release ~42%
- Process: content (~98%), parent (~2%)
- Trend: **slightly falling** — 4,243 (Jan 22–Feb 21) → 3,917 (Feb 21–Mar 22), ~8% decline. The `mio` update (2024485) was merged but 1916629 remains ASSIGNED, suggesting the fix needs further validation.

**Crash Details — [syscall | futex::futex_wait](https://crashes.mozilla.org/signatures?q=signature%3A%22syscall%20%7C%20std%3A%3Asys%3A%3Apal%3A%3Aunix%3A%3Afutex%3A%3Afutex_wait%22):**
- 7-day: **35** | 30-day: **182** crashes
- Platform: Linux (100%)
- Channels: ESR ~65%, Release ~29%
- Process: parent (100% in 7-day)
- Trend: **stable** (~6/day). Root cause is AudioIPC blocking the parent main thread during initialization.

**Timeline:** Bug 1916629 was filed September 2024. It became a topcrash as AudioIPC usage expanded. kinetik is triaging all three related fixes (2024485, 2024498, 1899317) simultaneously, with the longer-term goal of moving cubeb to a utility process.

---

### Theme 3 — AV1 Hardware Video Decode Failures

**User impact:** AV1 videos freeze, stutter, or fail to play — particularly at high bitrates (4K+) or on YouTube. Symptoms range from complete decode failure to periodic hangs when hardware acceleration is enabled via `media.ffvpx-hw.enabled`.

| Bug ID | Summary | Severity | Status | Last Changed |
|---|---|---|---|---|
| [1893427](https://bugzilla.mozilla.org/show_bug.cgi?id=1893427) | [Meta] Hardware accelerated video decoding through ffvpx — *Assigned: alwu* | N/A | NEW | 2025-12-14 |
| [1978183](https://bugzilla.mozilla.org/show_bug.cgi?id=1978183) | Enable `media.ffvpx-hw.enabled` by default on Windows — *Assigned: alwu* | N/A | NEW | 2026-03-16 |
| [2016484](https://bugzilla.mozilla.org/show_bug.cgi?id=2016484) | High-bitrate AV1 freezes: DAV1DDecoder busy-waits on dav1d EAGAIN | S2 | NEW | 2026-03-20 |
| [1978703](https://bugzilla.mozilla.org/show_bug.cgi?id=1978703) | AV1 video stuttering with media.ffvpx-hw.enabled (56 comments) | S3 | REOPENED | 2026-03-16 |
| [2008617](https://bugzilla.mozilla.org/show_bug.cgi?id=2008617) | 4K AV1 video decode doesn't work on YouTube | S3 | UNCONFIRMED | 2026-03-19 |
| [1884529](https://bugzilla.mozilla.org/show_bug.cgi?id=1884529) | [AMD RX 6700 XT] 4K AV1 on YouTube freezes | S3 | UNCONFIRMED | 2026-03-14 |
| [1793477](https://bugzilla.mozilla.org/show_bug.cgi?id=1793477) | AV1 Decoding in YouTube stutters on AMD Windows laptop (49 comments) — *Assigned: alwu* | S3 | UNCONFIRMED | 2025-11-25 |
| [2023159](https://bugzilla.mozilla.org/show_bug.cgi?id=2023159) | AV1-q perf regression (OSX) Mar 9 2026 | S3 | NEW | 2026-03-21 |
| [1936069](https://bugzilla.mozilla.org/show_bug.cgi?id=1936069) | YouTube AV1 buffering causes video to stop while audio continues | — | REOPENED | 2025-11-21 |
| [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) | Nvidia Tegra video HW decoding regression with Firefox 142+ | S3 | NEW | 2026-03-15 |

**Timeline:** AV1 hardware decode work began in 2024 via the ffvpx-hw meta (1893427). Bug 1978703 has been REOPENED after prior fixes failed to fully resolve the stutter, with 56 comments suggesting extended community investigation. The S2 bug 2016484 (dav1d busy-wait) was filed February 2026 and identifies a concrete busy-loop defect when `EAGAIN` is returned. The ffvpx-hw flag remains off by default pending bug 1978703 resolution. A macOS AV1 perf regression was detected in CI on March 9, 2026.

> **Stagnation note:** Bug [1978703](https://bugzilla.mozilla.org/show_bug.cgi?id=1978703) is REOPENED S3 with 56 comments and the most recent substantive change was 2026-03-16. It is actively looked at, but the REOPENED status indicates prior fixes were not sufficient.

---

### Theme 4 — HDR Video on Windows

**User impact:** Users cannot see HDR content on YouTube or other sites on Windows — video appears washed out, uses incorrect transfer functions, or HDR is not activated at all. Multiple hardware configurations affected (Intel, AMD, Qualcomm, Samsung). The feature is being actively developed.

| Bug ID | Summary | Severity | Status | Last Changed |
|---|---|---|---|---|
| [2012848](https://bugzilla.mozilla.org/show_bug.cgi?id=2012848) | [Meta] HDR video support on Windows follow-ups | — | NEW | 2026-03-20 |
| [2024683](https://bugzilla.mozilla.org/show_bug.cgi?id=2024683) | HDR on YouTube still broken on Win10 AMD RX 480 | S2 | NEW | 2026-03-20 |
| [2025015](https://bugzilla.mozilla.org/show_bug.cgi?id=2025015) | HDR doesn't work with software decoded video on Windows — *Assigned: jrmuizel* | — | NEW | 2026-03-22 |
| [2009596](https://bugzilla.mozilla.org/show_bug.cgi?id=2009596) | [HDR/Windows] Intel Iris Xe (Alder Lake Mobile) doesn't show HDR video | S3 | NEW | 2026-03-16 |
| [2009624](https://bugzilla.mozilla.org/show_bug.cgi?id=2009624) | HDR video transfer function mismatch on Qualcomm Snapdragon X1 | S3 | NEW | 2026-03-12 |
| [2011038](https://bugzilla.mozilla.org/show_bug.cgi?id=2011038) | HDR failure on Samsung laptop | — | NEW | 2026-03-19 |
| [1998608](https://bugzilla.mozilla.org/show_bug.cgi?id=1998608) | AV1 supported but still no HDR option on YouTube | S3 | UNCONFIRMED | 2026-03-14 |
| [2012850](https://bugzilla.mozilla.org/show_bug.cgi?id=2012850) | [HDR] Support HLG transfer function sources — *Assigned: ahale* | S3 | ASSIGNED | 2026-03-22 |
| [2023264](https://bugzilla.mozilla.org/show_bug.cgi?id=2023264) | We advertise HDR to YouTube when RGB10A2 overlay is not supported — *Assigned: ahale* | S3 | RESOLVED | 2026-03-17 |
| [2021018](https://bugzilla.mozilla.org/show_bug.cgi?id=2021018) | YouTube HDR video playback is dull on Windows — *Assigned: ahale* | — | RESOLVED | 2026-03-13 |

**Timeline:** HDR work on Windows accelerated in early 2026. Ashley Hale [:ahale] has been fixing issues rapidly (three RESOLVED bugs in March alone). However, new hardware-specific bugs continue to arrive: 2024683 (AMD RX 480, Win10) was filed March 19 and remains open S2. Bug 2025015 (software decode path) was just filed March 20 and assigned to Jeff Muizelaar. The meta (2012848) has 10 tracked follow-up items. HDR appears close to broad enablement but still has platform-specific regressions.

---

### Theme 5 — Android JNI Topcrash (libart/libmozglue)

**User impact:** Firefox for Android crashes in the content process via a JNI call path that traverses `libmozglue.so` → `libart.so`. This is a topcrash affecting the release population on Android.

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|---|---|---|---|---|---|
| [2023515](https://bugzilla.mozilla.org/show_bug.cgi?id=2023515) | Crash in `libc.so | <.plt ELF section in libmozglue.so> | libart.so | _JNIEnv::CallVoidMethodA | mozilla::jni::Method<T>::Call<T>` — *Assigned: jhlin* | S2 | NEW | 2026-03-21 | **738** |

**[Crash Signature](https://crashes.mozilla.org/signatures?q=signature%3A%22mozilla%3A%3Ajni%3A%3AMethod%22):**
- 30-day volume: **738** crashes
- Platform: Android (100%)
- Channel: release ~99%, beta ~1%
- Top versions: 148.0.2 (79%), 148.0.1 (12%)
- Process type: content (~97%), parent (~3%)
- Trend: Data dominated by the current release cycle, suggesting this is a regression in 148.x or newly surfaced on current Android devices.

**Timeline:** Filed March 16, 2026. Assigned immediately to John Lin [:jhlin]. The crash has `topcrash` keyword, confirming Socorro volume validation. The JNI call path suggests a media method dispatch issue in the content process.

---

### Theme 6 — captureStream API Shipping & Site Compat Impact

**User impact:** Several websites (pikimov.com, alfred.camera, app.kosmi.io) fail to work in Firefox because they rely on `HTMLMediaElement.captureStream()`, which was not spec-compliant or was disabled behind a pref. Firefox is actively shipping this feature in early 2026.

| Bug ID | Summary | Severity | Status | Last Changed |
|---|---|---|---|---|
| [1541471](https://bugzilla.mozilla.org/show_bug.cgi?id=1541471) | [Meta] Implement spec-compliant HTMLMediaElement.captureStream — *Assigned: alwu* | S3 | NEW | 2026-03-17 |
| [2007596](https://bugzilla.mozilla.org/show_bug.cgi?id=2007596) | Implement captureStream for HTMLMediaElement — *Assigned: alwu* | N/A | RESOLVED | 2026-03-06 |
| [2016216](https://bugzilla.mozilla.org/show_bug.cgi?id=2016216) | Enable `media.captureStream.enabled` by default on Nightly — *Assigned: alwu* | — | RESOLVED | 2026-03-19 |
| [2017708](https://bugzilla.mozilla.org/show_bug.cgi?id=2017708) | Enable `media.captureStream.enabled` by default — *Assigned: alwu* | — | RESOLVED | 2026-03-19 |
| [2010427](https://bugzilla.mozilla.org/show_bug.cgi?id=2010427) | Changing volume/mute on source element should not affect captured stream — *Assigned: alwu* | — | RESOLVED | 2026-03-06 |
| [1905866](https://bugzilla.mozilla.org/show_bug.cgi?id=1905866) | pikimov.com doesn't work in Firefox | S2 | NEW | 2025-09-15 |
| [1942763](https://bugzilla.mozilla.org/show_bug.cgi?id=1942763) | alfred.camera — "Unsupported browser" | S2 | NEW | 2026-03-02 |
| [1963270](https://bugzilla.mozilla.org/show_bug.cgi?id=1963270) | app.kosmi.io — Missing "Local file" option — *Assigned: twisniewski* | S2 | ASSIGNED | 2026-03-16 |
| [1336401](https://bugzilla.mozilla.org/show_bug.cgi?id=1336401) | Remove HTMLMediaElement::mozCaptureStream (old API) — *Assigned: alwu* | S3 | NEW | 2026-01-06 |
| [2009488](https://bugzilla.mozilla.org/show_bug.cgi?id=2009488) | Don't recreate DecodedStream when removing audio output — *Assigned: alwu* | — | NEW | 2026-01-09 |

**Timeline:** The captureStream meta (1541471) has been open since 2019. Alastor Wu [:alwu] drove the implementation in late 2025 / early 2026, landing the core implementation (2007596, RESOLVED P2), and enabling the pref on both Nightly (2016216) and stable (2017708) in February/March 2026. Three S2 site-compat bugs remain open — these will resolve once the feature ships to users broadly. This is primarily a success story with a few remaining loose ends.

---

### Theme 7 — Linux Audio: PipeWire / ALSA / cubeb

**User impact:** Linux users experience persistent audio interface activation even when nothing is playing (PipeWire), microphone failures (ALSA), audio streams staying open on pause, and a parent-process crash in the audio subsystem.

| Bug ID | Summary | Severity | Status | Last Changed |
|---|---|---|---|---|
| [1984881](https://bugzilla.mozilla.org/show_bug.cgi?id=1984881) | x.com causes audio interface to open (PipeWire) despite nothing playing — *Assigned: karlt* | S3 | NEW | 2026-03-18 |
| [2002450](https://bugzilla.mozilla.org/show_bug.cgi?id=2002450) | Remove AudioDestinationNode audio output when no active input (fix) — *Assigned: karlt* | — | ASSIGNED | 2026-03-18 |
| [2022993](https://bugzilla.mozilla.org/show_bug.cgi?id=2022993) | Crash `syscall | futex::futex_wait` — Linux parent crash — *Assigned: kinetik* | S2 | ASSIGNED | 2026-03-18 |
| [1716249](https://bugzilla.mozilla.org/show_bug.cgi?id=1716249) | Selecting default input device — ALSA/Linux | S4 | UNCONFIRMED | 2026-03-19 |
| [1650131](https://bugzilla.mozilla.org/show_bug.cgi?id=1650131) | Microphone doesn't work on Linux with ALSA | S4 | UNCONFIRMED | 2026-03-19 |
| [1959613](https://bugzilla.mozilla.org/show_bug.cgi?id=1959613) | Audio stream remains open when playback is paused | S4 | UNCONFIRMED | 2026-03-18 |

**Timeline:** The PipeWire "always-open" issue (1984881) was filed August 2025; Karl Tomlinson [:karlt] is implementing the fix in 2002450 by removing the output track when there is no active input for a period. The ALSA microphone and default device bugs are older (2020–2021) but saw new activity during this window, suggesting they remain unsatisfying for Linux users. The Linux futex crash (182 in 30 days) is being addressed alongside the Windows AudioIPC work.

---

### Theme 8 — GMP / DRM / AppLocker Stability

**User impact:** Encrypted video (Widevine, PlayReady) fails to play or crashes on certain Windows enterprise configurations (AppLocker), in Amazon Prime, or when switching audio tracks. The GMP loader crash has been accumulating reports since 2023.

| Bug ID | Summary | Severity | Status | Last Changed |
|---|---|---|---|---|
| [2023094](https://bugzilla.mozilla.org/show_bug.cgi?id=2023094) | AppLocker Publisher rules don't work with USER_RESTRICTED token (GMP) — *Assigned: bobowen* | S3 | ASSIGNED | 2026-03-17 |
| [1830431](https://bugzilla.mozilla.org/show_bug.cgi?id=1830431) | Crash in `mozilla::gmp::GMPLoader::Load` (44 comments) | S3 | NEW | 2026-03-13 |
| [1768038](https://bugzilla.mozilla.org/show_bug.cgi?id=1768038) | GMP (Widevine) crashes on Amazon Prime (regression) | S3 | NEW | 2026-02-16 |
| [1972665](https://bugzilla.mozilla.org/show_bug.cgi?id=1972665) | Audio dies when switching audio tracks (Widevine, Desktop only) | S3 | UNCONFIRMED | 2026-03-18 |
| [1962665](https://bugzilla.mozilla.org/show_bug.cgi?id=1962665) | Firefox and PlayReady: video is black but audio is ok (dashjs) | S3 | UNCONFIRMED | 2026-03-19 |

**Timeline:** The GMPLoader::Load crash (1830431) is a long-standing issue with 44 comments. The AppLocker bug (2023094) is a P1 fix being driven by Bob Owen [:bobowen] — it was filed March 13 and directly depends on 1830431. Once 2023094 lands, it may significantly reduce the GMPLoader crash signal. The Widevine audio-track bug (1972665) and PlayReady black-screen bug (1962665) are unowned S3 regressions with no current assignees.

---

### Theme 9 — Video A/V Sync & MSE

**User impact:** Audio and video fall out of sync in specific scenarios: YouTube playback at 2× speed, looped MSE media, and high-bitrate streams. MSE TimeUnit overflow can cause silent playback corruption.

| Bug ID | Summary | Severity | Status | Last Changed |
|---|---|---|---|---|
| [1498733](https://bugzilla.mozilla.org/show_bug.cgi?id=1498733) | [Meta] Seamless media playback looping | S3 | NEW | 2026-03-21 |
| [1955841](https://bugzilla.mozilla.org/show_bug.cgi?id=1955841) | Video and audio gets out of sync at 2× on YouTube (regression) | S3 | NEW | 2026-03-22 |
| [2023823](https://bugzilla.mozilla.org/show_bug.cgi?id=2023823) | MSE audio track desyncs from video on loop seek via ended event | S3 | UNCONFIRMED | 2026-03-21 |
| [2017567](https://bugzilla.mozilla.org/show_bug.cgi?id=2017567) | Handle more TimeUnit overflow cases in MSE — *Assigned: padenot* | S3 | NEW | 2026-03-17 |
| [1936069](https://bugzilla.mozilla.org/show_bug.cgi?id=1936069) | YouTube AV1 buffering causes video to stop while audio continues | — | REOPENED | 2025-11-21 |

**Timeline:** The seamless looping meta (1498733) was created in 2018 and gained a new dep (2023823) in March 2026 — fresh user reports of MSE loop desync. Bug 1955841 is a regression for 2× speed playback filed March 2025 with `nightly-community` validation, currently unowned. Paul Adenot [:padenot] is working on TimeUnit overflow (2017567), which is a prerequisite for some looping fixes.

---

### Theme 10 — Media Memory Leaks & Performance

**User impact:** Firefox leaks memory during prolonged video playback (F1TV, rapid audio replay), generates excessive heat watching YouTube, and causes parent-process jank when hovering over videos in Google Drive.

| Bug ID | Summary | Severity | Status | Last Changed |
|---|---|---|---|---|
| [1950282](https://bugzilla.mozilla.org/show_bug.cgi?id=1950282) | f1tv.formula1.com — "Firefox is not a supported browser" (site compat + memory leak) — *Assigned: twisniewski* | S2 | ASSIGNED | 2026-02-16 |
| [1992579](https://bugzilla.mozilla.org/show_bug.cgi?id=1992579) | Memory leak with F1TV | S3 | NEW | 2026-03-21 |
| [1999639](https://bugzilla.mozilla.org/show_bug.cgi?id=1999639) | Rapid audio playback causes audiodg to use multiple GB RAM on Windows | S3 | NEW | 2026-03-16 |
| [2023447](https://bugzilla.mozilla.org/show_bug.cgi?id=2023447) | High power consumption and heat playing YouTube videos | S3 | UNCONFIRMED | 2026-03-16 |
| [1903051](https://bugzilla.mozilla.org/show_bug.cgi?id=1903051) | Massive parent process jank when hovering over video in Google Drive | S3 | NEW | 2026-03-18 |

> **Stagnation note:** Bug [1950282](https://bugzilla.mozilla.org/show_bug.cgi?id=1950282) is S2/P1 (F1TV) and was last changed **2026-02-16** — **34 days ago** with no recent activity. Given its P1 rating, this warrants attention.

**Timeline:** The F1TV memory leak (1992579) and site compat bug (1950282) are related — the memory leak may be causing the site to consider Firefox incompatible. The audiodg Windows leak (1999639) is new (November 2025) and unowned. The parent-process jank (1903051) is related to the cubeb utility process work (1899317), where audio processing on the parent thread causes observed freezes.

---

## Emerging Themes to Watch

These themes have early-stage signal but represent potentially significant issues:

**Audio Device Name PII Leakage** — Bug [2023970](https://bugzilla.mozilla.org/show_bug.cgi?id=2023970) (S2, P2, Web Audio): `about:support` exposes potentially sensitive audio device names (e.g., company conference room names, home network device names). Filed March 17, 2026. No assignee yet.

**Autoplay & Screensaver Meta Bugs** — Two new meta bugs were created on 2026-03-14: [2023365](https://bugzilla.mozilla.org/show_bug.cgi?id=2023365) ([Meta] Auto Play Issues) and [2023379](https://bugzilla.mozilla.org/show_bug.cgi?id=2023379) ([Meta] Media Related Sleep Issues). The screensaver inhibition bug (2013720, Linux Mint) is part of the latter with 16 tracked dependencies.

**Nvidia Tegra HW Decode Regression** — Bug [2016587](https://bugzilla.mozilla.org/show_bug.cgi?id=2016587) (S3, P3): Hardware video decode regressed on Nvidia Tegra-based devices starting with Firefox 142+. Filed February 2026, unowned.

**Video Rotation Color Shift** — Bug [2023594](https://bugzilla.mozilla.org/show_bug.cgi?id=2023594) (S3, regression, Web Codecs): Applying a CSS/transform rotation to a video causes colors to shift — a regression in the WebCodecs pipeline. Filed March 16, 2026, 13 comments, unowned.

---

## Closing

### Ranked Signal Summary

| Rank | Theme | Breadcrumbs | Meta Bug | Top Severity | Notes |
|---|---|---|---|---|---|
| 1 | Bluetooth Audio Disruption | 25 | [2011679](https://bugzilla.mozilla.org/show_bug.cgi?id=2011679) | S2 | 23 independent reporters; assigned to kinetik; cross-platform |
| 2 | Windows Named Pipe / AudioIPC Crash | 6 | — | S2 | 3,917 crashes/30d; topcrash; fix in progress (kinetik) |
| 3 | Android JNI Topcrash | 1 (+ 738 crash reports) | — | S2 | 738 crashes/30d; topcrash; assigned to jhlin |
| 4 | AV1 / HW Video Decode Failures | 10 | [1893427](https://bugzilla.mozilla.org/show_bug.cgi?id=1893427) | S2 | Multiple user-facing failures; S2 busy-wait bug; ff-vpx-hw blocked |
| 5 | HDR Video on Windows | 10 | [2012848](https://bugzilla.mozilla.org/show_bug.cgi?id=2012848) | S2 | Active development; S2 AMD bug remains open; shipping imminent |
| 6 | captureStream Shipping / Site Compat | 10 | [1541471](https://bugzilla.mozilla.org/show_bug.cgi?id=1541471) | S2 | 3 S2 site-compat bugs; pref enabled Nightly; alwu driving |
| 7 | Linux Audio: PipeWire/ALSA/cubeb | 6 | — | S2 | futex crash 182/30d; PipeWire "always open" fix in progress |
| 8 | GMP / DRM / AppLocker | 5 | — | S3 | P1 AppLocker fix (bobowen); GMPLoader crash ongoing |
| 9 | Video A/V Sync & MSE | 5 | [1498733](https://bugzilla.mozilla.org/show_bug.cgi?id=1498733) | S3 | P2 regression at 2× speed; MSE loop desync; TimeUnit fix pending |
| 10 | Media Memory Leaks & Performance | 5 | — | S2 | P1 F1TV S2 stagnant 34d; audiodg leak unowned |

---

### Resources Used

- **Bugzilla REST API:** 9 fetch calls (2 seed queries, 4 dep/meta batch fetches, 3 keyword expansion queries)
- **Socorro SuperSearch API:** 8 calls covering 4 crash signatures with trend windows
- **Dep crawl depth:** Depth 2 (Bluetooth meta deps, captureStream meta deps, other dep/block IDs)
- **Total unique bugs examined:** ~130 across all components and products

### Suggestions for Skill Improvement

1. **Crash signature auto-discovery:** When a bug has a `crash` keyword and the summary contains a partial signature, automatically construct the Socorro search URL rather than requiring manual signature extraction.
2. **Stagnation baseline computation:** Automate the calculation of "days since last change" and flag stagnant S1/S2 bugs as a structured scan rather than scanning manually.
3. **cc_count enrichment pass:** The Bugzilla API frequently omits `cc_count` from batch responses. Building in an automatic secondary enrichment pass for any bugs missing it would improve signal accuracy.
4. **Reporter diversity scoring:** A simple heuristic — counting unique email domains in bug comments — would allow more precise separation of "one forum thread triggered 20 reports" from "20 independent users found this independently."

---

*"The world is full of obvious things which nobody by any chance ever observes."*
*— Sherlock Holmes (A. Conan Doyle)*
