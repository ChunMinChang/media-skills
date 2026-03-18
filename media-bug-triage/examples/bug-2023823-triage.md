# Bug 2023823 Triage Analysis

**Generated:** 2026-03-17
**Bug URL:** https://bugzilla.mozilla.org/show_bug.cgi?id=2023823

## Bug Information

- **Summary:** MSE audio track desyncs from video on loop seek via ended event, while manual seek to same timestamp works correctly
- **Reporter:** alex.servanis@proton.me (external)
- **Status:** UNCONFIRMED
- **Product:** Core
- **Component:** Audio/Video: Playback
- **Created:** 2026-03-17
- **Severity:** -- (not set)
- **Priority:** -- (not set)

## Research Summary and Key Findings

The reporter describes an intermittent MSE audio/video desynchronization bug triggered specifically when a YouTube video (30+ minutes) loops back to the beginning. The core symptom: the video track correctly returns to `0:00` but the audio track lands at an incorrect position — typically around the 14-minute mark. Three failure modes were observed: audio starting at ~14-minute mark, silent audio, and video glitching to an arbitrary timestamp near end-of-file.

The reporter's key diagnostic finding is that a manual user-initiated seek to `0:00` (via the progress bar) immediately repairs the desync, confirming audio data from the beginning is present in the SourceBuffer and not evicted. They explicitly ruled out buffer eviction by increasing `media.mediasource.eviction_threshold.video` and `media.mediasource.eviction_threshold.audio` to very large values. Post-change, video consistently loops to `0:00`, but audio desync persists — confirming this is a **seek coordination problem** between the audio and video SourceBuffers, not a buffer management issue. The intermittent nature is consistent with a race condition.

**Related bugs found:**
- [1950599](https://bugzilla.mozilla.org/show_bug.cgi?id=1950599) — "Looping a video on YouTube has a high chance causing the video/audio to completely mismatch" (UNCONFIRMED, S4, 2025-02-26). Describes the same scenario: YouTube loop causes A/V mismatch, with video frozen on a frame ahead while audio catches up (~18 seconds out of sync). Codec-agnostic (H.264 and AV1), unaffected by hardware acceleration toggle. Likely the same root cause; 1950599 is the older report. A Firefox profiler profile was attached to 1950599.
- [1898182](https://bugzilla.mozilla.org/show_bug.cgi?id=1898182) — WPT test `mediasource-seek-during-pending-seek.html` has intermittent failures on Android. This test exercises seeking while a seek is already pending in MSE — directly related to the race condition suspected here.
- [1976403](https://bugzilla.mozilla.org/show_bug.cgi?id=1976403) — YouTube videos unexpectedly looping due to Bose Bluetooth headphones sending spurious AVRCP events via `media.hardwaremediakeys.enabled`; different root cause, not a duplicate.

## Regression Timeline

Not reported as a regression. No mozregression data or Firefox version bisection available. Bug 1950599 (same symptom) was filed 2025-02-26 against Firefox 135, suggesting this issue has existed for over a year.

## Classification

| Signal | Detected | Evidence |
|--------|----------|----------|
| Clear STR | Partial | Steps documented, but issue is intermittent (~50% repro); requires 30+ min YouTube video + loop |
| Test Case | No | No attached test file |
| Crash Stack | No | Not a crash |
| Fuzzing | No | — |

## Assessment

- **Suggested Severity:** S3
- **Suggested Priority:** P3

### Assessment Reasoning

The bug blocks the loop-playback functionality for MSE-based content, but a workaround exists (manually seek to `0:00` after the desync occurs). The issue is intermittent and limited to YouTube-style long-form MSE video content. It does not affect basic playback or cause data loss. S3 is appropriate.

P3 reflects that this is a real, reproducible-in-principle issue that has been present for at least a year (see bug 1950599 filed 2025-02-26 with the same symptom), but does not rise to P1/P2 given the intermittency and available workaround.

Bug 1950599 should be evaluated as a potential duplicate — it is the older report describing the same MSE loop A/V desync symptom. If confirmed as the same issue, 2023823 should be duped to 1950599.

## Codebase Investigation

Firefox's seamless looping path is controlled by `media.seamless-looping-video` (default: `true`). When enabled, the `MediaDecoderStateMachine` transitions to `LoopingDecodingState` (defined in [MediaDecoderStateMachine.cpp](https://searchfox.org/mozilla-central/source/dom/media/MediaDecoderStateMachine.cpp)) when a looping video reaches EOS.

`LoopingDecodingState::RequestDataFromStartPosition` seeks each track independently back to `TimeUnit::Zero()` using per-track `SeekTarget::Track::AudioOnly` / `VideoOnly` seeks on the `MediaFormatReader`. A serialization mechanism (`mPendingSeekingType`) defers the second track's seek until the first completes. However, the `mOriginalDecodedDuration` calculation — which sets the queue time offset for subsequent loops — must be accurate and ready before both tracks re-enter the decoding state. If `DetermineOriginalDecodedDurationIfNeeded` fails to resolve the duration (e.g., because audio and video EOS are reached asynchronously), the queue offsets can be mismatched, causing a desync.

An alternative code path applies when the native `loop` attribute is NOT used and YouTube's JavaScript intercepts the `ended` event and calls `video.currentTime = 0`. In this case, the seek goes through `AccurateSeekingState` rather than `LoopingDecodingState`. The behavior of `TrackBuffersManager::Seek` (in [TrackBuffersManager.cpp](https://searchfox.org/mozilla-central/source/dom/media/mediasource/TrackBuffersManager.cpp)) when seeking during or immediately after a track-level EOS condition may differ from a seek during normal playback.

The intermittent WPT failures on `mediasource-seek-during-pending-seek.html` (bug 1898182) are notable — this test exercises seeking during a pending seek, which is the race window described by the reporter.

## Suggested Investigation Areas

1. **`LoopingDecodingState::RequestDataFromStartPosition`** (~line 1083, [MediaDecoderStateMachine.cpp](https://searchfox.org/mozilla-central/source/dom/media/MediaDecoderStateMachine.cpp)) — verify the audio/video seek serialization is correct and that `mOriginalDecodedDuration` is set before queue offsets are adjusted.
2. **`LoopingDecodingState::DetermineOriginalDecodedDurationIfNeeded`** — check whether duration determination can fail or be incomplete when audio and video tracks reach EOS at different times (common in MSE with separate SourceBuffers).
3. **`TrackBuffersManager::Seek`** ([TrackBuffersManager.cpp](https://searchfox.org/mozilla-central/source/dom/media/mediasource/TrackBuffersManager.cpp)) — examine behavior when called immediately after a track reaches EOS; there is a special path for empty track buffers (returns `TimeUnit::Zero()` with a reset) that may interact poorly with the per-track seek timing.
4. **`media.seamless-looping-video` pref** — asking the reporter to toggle this pref to `false` and observe whether the desync still occurs would disambiguate between the `LoopingDecodingState` path and the regular `AccurateSeekingState` path.

## Suggested Feedback Request

Request a media playback log via `about:logging` while reproducing the desync. Also ask the reporter to try toggling `media.seamless-looping-video` to `false` in `about:config` to see if it changes the behavior. This would confirm which code path is involved.

---

```
Thank you for this detailed and well-investigated bug report!

To help us narrow down the root cause, could you please try the following:

1. **Toggle media.seamless-looping-video**: In `about:config`, set `media.seamless-looping-video` to `false` and repeat the test. Does the audio desync still occur? This will help us identify which looping code path is involved.

2. **Capture a media playback log**:
   - Navigate to `about:logging`
   - In the preset dropdown, select "Media playback" and click "Set Log Modules"
   - Click "Start Logging"
   - Reproduce the desync (loop a 30+ min YouTube video until it fails)
   - Stop logging and share the profile URL here

This information will be very useful for tracking down the exact point where audio and video diverge during the loop seek.
```

## Bugzilla Use Tracking

- Total Bugzilla Queries: 14
- Total Bugs Processed: 8
- Estimated Download Bandwidth Used: ~0.3 MB
- Inaccessible Bugs Due to Permissions: 0
