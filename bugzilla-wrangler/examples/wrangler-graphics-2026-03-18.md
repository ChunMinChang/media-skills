# Firefox Graphics Bug Wrangler Report

---

## Session Info

| Field | Value |
|-------|-------|
| **Date** | 2026-03-18 |
| **Scope** | graphics |
| **Components** | Core :: Graphics, Graphics: WebRender, Graphics: CanvasWebGL, Graphics: Layers, Graphics: Text, Canvas: 2D, Layout: Painting, CSS Painting and Compositing |
| **Seed timeframe** | 2025-12-18 to 2026-03-18 (90 days) |
| **Seed count** | 50 |
| **Seed mode** | mixed-seed (37 created + 13 changed = 50 unique) |
| **Cache freshness** | Written this session (2026-03-18) |

---

## Seed Info

### Bug List (by priority, then creation date)

**P2 bugs (3):**
- [2020096](https://bugzilla.mozilla.org/show_bug.cgi?id=2020096) — large SVG consumes all system resources (S2, Graphics)
- [2020195](https://bugzilla.mozilla.org/show_bug.cgi?id=2020195) — Canvas displays screen content from other applications due to NVIDIA/dmabuf (S2, Graphics: CanvasWebGL, sec-vector)
- [2020844](https://bugzilla.mozilla.org/show_bug.cgi?id=2020844) — macOS - With Layer Compositor enabled, Large parts of UI glitch (S2, Graphics: WebRender)

**P3 bugs (15):**
- [2020981](https://bugzilla.mozilla.org/show_bug.cgi?id=2020981) — 39.23-4.23% bing-search FirstVisualChange regression (S3, WebRender, perf-alert)
- [2020923](https://bugzilla.mozilla.org/show_bug.cgi?id=2020923) — Remove remaining usage of non-quad gradients (S3, WebRender)
- [2020192](https://bugzilla.mozilla.org/show_bug.cgi?id=2020192) — Frame rate is limited to the monitor with lowest FPS (S3, WebRender)
- [2023466](https://bugzilla.mozilla.org/show_bug.cgi?id=2023466) — Pop out window is faded, or has greyish cast (S3, WebRender)
- [2023886](https://bugzilla.mozilla.org/show_bug.cgi?id=2023886) — Port normal borders from brush to quads (S3, WebRender)
- [2020420](https://bugzilla.mozilla.org/show_bug.cgi?id=2020420) — Fullscreen mode goes black in Youtube with hardware acceleration (S3, Graphics)
- [2019903](https://bugzilla.mozilla.org/show_bug.cgi?id=2019903) — shutdownhang FT_Stream_ReadULong (S3, Graphics: Text)
- [1965442](https://bugzilla.mozilla.org/show_bug.cgi?id=1965442) — Freezing on text input or pausing/playing a video (S3, WebRender, 18 comments)
- [1887835](https://bugzilla.mozilla.org/show_bug.cgi?id=1887835) — [meta] [project] Quad shaders (S3, WebRender, meta)
- [1988728](https://bugzilla.mozilla.org/show_bug.cgi?id=1988728) — backdrop-filter: blur is laggy when GPU acceleration isn't available (S3, WebRender, P2)
- [1799334](https://bugzilla.mozilla.org/show_bug.cgi?id=1799334) — backdrop-filter doesn't blur remote `<browser>` element (S3, WebRender, P2)
- [2002404](https://bugzilla.mozilla.org/show_bug.cgi?id=2002404) — Selecting a menu option from the hamburger menu activates video playback (S3, WebRender)
- [1997150](https://bugzilla.mozilla.org/show_bug.cgi?id=1997150) — Image upsampling is not gamma-correct (S3, Graphics)
- [1985706](https://bugzilla.mozilla.org/show_bug.cgi?id=1985706) — Full-page screenshots show a 1px dark line after recent Firefox update (S3, Graphics, 16 comments)
- [2005440](https://bugzilla.mozilla.org/show_bug.cgi?id=2005440) — [Regression] Emojis fail to render on macOS (aarch64) in Lockdown mode (S3, Graphics, ASSIGNED, 27 comments)

**P-- / untriaged bugs (32):**
- [2013967](https://bugzilla.mozilla.org/show_bug.cgi?id=2013967) — 3d transforms don't display correctly with opacity and rotation (S2, stalled, regression)
- [2019679](https://bugzilla.mozilla.org/show_bug.cgi?id=2019679) — WebRender GPU texture corruption and memory leak on NVIDIA RTX 40 series (S2, WebRender)
- [2008637](https://bugzilla.mozilla.org/show_bug.cgi?id=2008637) — Integer overflow in ShmSegmentsReader → release-assert crash (S3, reporter-external, csectype-intoverflow)
- [2021699](https://bugzilla.mozilla.org/show_bug.cgi?id=2021699) — Stack exhaustion in FreeType load_truetype_glyph() (S3, crash, csectype-dos, reporter-external)
- [2021972](https://bugzilla.mozilla.org/show_bug.cgi?id=2021972) — Hit MOZ_CRASH(ElementAt) at Assertions.cpp (S3, regression, bugmon)
- [2022521](https://bugzilla.mozilla.org/show_bug.cgi?id=2022521) — backdrop-filter via Tailwind renders incorrectly on modal overlays (S3, WebRender)
- [2016655](https://bugzilla.mozilla.org/show_bug.cgi?id=2016655) — Mixed rendering of background-attachment: Fixed and backdrop-filter broken (S3, WebRender)
- [2016821](https://bugzilla.mozilla.org/show_bug.cgi?id=2016821) — Blurry text, which becomes sharp when selecting (S3, Graphics: Text)
- [2018607](https://bugzilla.mozilla.org/show_bug.cgi?id=2018607) — SVG backdrop-filter won't apply feTurbulence/feDisplacementMap (S3, Graphics)
- [2013247](https://bugzilla.mozilla.org/show_bug.cgi?id=2013247) — Crash in TileCacheInstance::setup_compositor_surfaces_impl (S3, crash, 19 Socorro reports)
- [2013674](https://bugzilla.mozilla.org/show_bug.cgi?id=2013674) — memory leak (S3, Graphics, 10 comments)
- [2018463](https://bugzilla.mozilla.org/show_bug.cgi?id=2018463) — Firefox Nightly Linux font rendering is blurry (S3, Graphics)
- [2019155](https://bugzilla.mozilla.org/show_bug.cgi?id=2019155) — Valid WebGL2 shaders get link error on Windows only (S3, WebRender)
- [2019786](https://bugzilla.mozilla.org/show_bug.cgi?id=2019786) — wrench-deps jobs permafailing on ESR115 (S4, WebRender)
- [2011453](https://bugzilla.mozilla.org/show_bug.cgi?id=2011453) — Visible round border between picked color and dark background (S3, regression, 12 comments)
- [2016487](https://bugzilla.mozilla.org/show_bug.cgi?id=2016487) — Hit MOZ_CRASH at gpu_buffer.rs:446 (S3, crash, pernosco)
- [2015471](https://bugzilla.mozilla.org/show_bug.cgi?id=2015471) — Crash in [@ memcpy | FT_Stream_ReadAt] (S3, crash)
- [2015437](https://bugzilla.mozilla.org/show_bug.cgi?id=2015437) — Crash in dri2_allocate_textures on Raspbian (S3, crash, 9 Socorro reports)
- [2015602](https://bugzilla.mozilla.org/show_bug.cgi?id=2015602) — Significant performance issue with complex SVG at blowfish.page (S3)
- [2015955](https://bugzilla.mozilla.org/show_bug.cgi?id=2015955) — Large event jank from synchronous image decoding in Kotlin-wasm (S3)
- [2017580](https://bugzilla.mozilla.org/show_bug.cgi?id=2017580) — GPU process memory growth with Foundry Virtual Tabletop (S3)
- [2017679](https://bugzilla.mozilla.org/show_bug.cgi?id=2017679) — calc() in SVG rect x/y attributes renders incorrectly (S3)
- [2018404](https://bugzilla.mozilla.org/show_bug.cgi?id=2018404) — webgl: INVALID_ENUM vs INVALID_VALUE for OOB activeTexture (S3)
- [2008381](https://bugzilla.mozilla.org/show_bug.cgi?id=2008381) — Hit MOZ_CRASH(explicit panic) at render_task.rs:45 (S3, regression)
- [2012337](https://bugzilla.mozilla.org/show_bug.cgi?id=2012337) — Severe scrolling lag on Rockstar Games GTA VI website (S3)
- [2010645](https://bugzilla.mozilla.org/show_bug.cgi?id=2010645) — WebGL Google map turns black after zooming in and out (S3)
- [2014745](https://bugzilla.mozilla.org/show_bug.cgi?id=2014745) — WEBRENDER_SCISSORED_CACHE_CLEARS is disabled (S4)
- [1769944](https://bugzilla.mozilla.org/show_bug.cgi?id=1769944) — Credit Card backdrop-filter animation uses 2x more GPU than Chrome (S3)
- [1806281](https://bugzilla.mozilla.org/show_bug.cgi?id=1806281) — Codepen image is blurry (perspective ChooseScale) (S3, ASSIGNED)
- [1582153](https://bugzilla.mozilla.org/show_bug.cgi?id=1582153) — [meta] Improve blob rendering performance (S2, meta)
- [1996466](https://bugzilla.mozilla.org/show_bug.cgi?id=1996466) — Firefox freezes or temporarily crashes when opening site from history (S3, 13 comments)
- [1996466](https://bugzilla.mozilla.org/show_bug.cgi?id=1996466) — see above (duplicate line removed)

### Seed Creation Timeline

Distribution of seed bugs created within the seed window by month:

```
Dec 2025  [                    ] 0
Jan 2026  [███████             ] 7  ● ● ● ● ● ● ●
Feb 2026  [███████████████████ ] 19 ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●
Mar 2026  [███████████         ] 11 ● ● ● ● ● ● ● ● ● ● ●
                                   1st          18th
```

> Note: No bugs from December 2025 in the seed. The window opened mid-December and the first relevant bugs appear in early January. The seed is representative of Q1 2026 activity with a clear ramp from January through mid-March.

---

## Themes

---

### Theme 1: backdrop-filter Correctness and Performance

**User-facing impact:** Users see incorrect or missing blur/filter effects behind elements styled with `backdrop-filter`, particularly on modal dialogs, sidebars, cards, and page overlays. The issue is pervasive across frameworks (Tailwind, plain CSS) and affects multiple OS/GPU combinations. In some cases the filter is missing entirely; in others it conflicts with ancestor filters, produces visual artifacts, uses excessive GPU, or is absent in WebExtension screenshots. This is one of the most reported CSS rendering pain points in Firefox.

**Meta coverage:**
- [1888025](https://bugzilla.mozilla.org/show_bug.cgi?id=1888025) — [meta] Fix correctness issues with backdrop-filter (S3, **51 open deps**)
- [1888024](https://bugzilla.mozilla.org/show_bug.cgi?id=1888024) — [meta] Fix performance issues with backdrop-filter (S2, 9 deps)

**Breadcrumb table:**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2024163](https://bugzilla.mozilla.org/show_bug.cgi?id=2024163) | Hairline pixel artifact using backdrop-filter | -- | NEW | 2026-03-18 |
| [2022521](https://bugzilla.mozilla.org/show_bug.cgi?id=2022521) | backdrop-filter via Tailwind renders incorrectly on modal overlays | S3 | UNCONFIRMED | 2026-03-12 |
| [2016655](https://bugzilla.mozilla.org/show_bug.cgi?id=2016655) | Mixed rendering of background-attachment: Fixed and backdrop-filter broken | S3 | NEW | 2026-03-13 |
| [2018607](https://bugzilla.mozilla.org/show_bug.cgi?id=2018607) | SVG backdrop-filter won't apply feTurbulence/feDisplacementMap | S3 | UNCONFIRMED | 2026-02-24 |
| [2011747](https://bugzilla.mozilla.org/show_bug.cgi?id=2011747) | backdrop-filter fails to render if ancestor has drop-shadow/blur filter (webcompat:platform-bug) | S3 | NEW | 2026-02-07 |
| [1988728](https://bugzilla.mozilla.org/show_bug.cgi?id=1988728) | backdrop-filter: blur is laggy when GPU acceleration isn't available | S3 | UNCONFIRMED | 2026-03-17 |
| [1799334](https://bugzilla.mozilla.org/show_bug.cgi?id=1799334) | backdrop-filter doesn't blur remote `<browser>` element | S3 | UNCONFIRMED | 2026-03-17 |
| [1769944](https://bugzilla.mozilla.org/show_bug.cgi?id=1769944) | Credit Card backdrop-filter animation uses 2x more GPU than Chrome | S3 | UNCONFIRMED | 2026-03-17 |
| [1888025](https://bugzilla.mozilla.org/show_bug.cgi?id=1888025) | [meta] Fix correctness issues with backdrop-filter (51 deps) | S3 | NEW | 2026-03-12 |
| [1888024](https://bugzilla.mozilla.org/show_bug.cgi?id=1888024) | [meta] Fix performance issues with backdrop-filter (9 deps) | S2 | NEW | 2025-12-05 |
| [1657997](https://bugzilla.mozilla.org/show_bug.cgi?id=1657997) | Screenshot doesn't capture backdrop-filter effects | S3 | NEW | 2026-01-03 |
| [1852198](https://bugzilla.mozilla.org/show_bug.cgi?id=1852198) | backdrop-filter breaks bottom rounded corners on Linux | S3 | NEW | 2025-12-02 |
| [2009373](https://bugzilla.mozilla.org/show_bug.cgi?id=2009373) | backdrop-filter conflicts with Nvidia VSR | S3 | UNCONFIRMED | 2026-01-17 |

**Timeline:** The correctness meta-bug [1888025](https://bugzilla.mozilla.org/show_bug.cgi?id=1888025) was created in March 2024 and has accumulated 51 open dependency bugs over two years — indicating endemic, unresolved fragmentation in backdrop-filter rendering. The performance meta [1888024](https://bugzilla.mozilla.org/show_bug.cgi?id=1888024) (S2) has not changed since December 2025. New user-filed issues continue to arrive in 2026 (2022521 in March, 2024163 filed today). The dep graph has not been significantly drained. No clear assignee on either meta.

---

### Theme 2: SVG Rendering Regressions and Performance

**User-facing impact:** SVG content is broken in several distinct ways: a large SVG can lock up the browser and exhaust system resources; fill attribute changes during SVG animation can corrupt unrelated path rendering; `feOffset` shadow effects are drawn incorrectly; `calc()` in SVG geometry attributes renders wrong; and complex SVGs cause sustained CPU spikes. These affect SVG-heavy sites (maps, diagrams, games) as well as authoring tools.

**Breadcrumb table:**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2020096](https://bugzilla.mozilla.org/show_bug.cgi?id=2020096) | large SVG consumes all system resources | S2, P2 | NEW | 2026-03-17 |
| [2023989](https://bugzilla.mozilla.org/show_bug.cgi?id=2023989) | SVG feOffset shadow-effect drawn in wrong place, broken invalidation (regression) | -- | NEW | 2026-03-18 |
| [2022954](https://bugzilla.mozilla.org/show_bug.cgi?id=2022954) | Changing SVG fill attribute breaks display of another path (regression, nightly-community) | -- | NEW | 2026-03-14 |
| [2017679](https://bugzilla.mozilla.org/show_bug.cgi?id=2017679) | calc() in SVG rect x/y attributes renders incorrectly | S3 | UNCONFIRMED | 2026-02-19 |
| [2015602](https://bugzilla.mozilla.org/show_bug.cgi?id=2015602) | Significant performance issue with complex SVG at blowfish.page | S3 | UNCONFIRMED | 2026-02-20 |
| [2018607](https://bugzilla.mozilla.org/show_bug.cgi?id=2018607) | SVG backdrop-filter won't apply feTurbulence/feDisplacementMap | S3 | UNCONFIRMED | 2026-02-24 |
| [1582153](https://bugzilla.mozilla.org/show_bug.cgi?id=1582153) | [meta] Improve blob rendering performance (S2, P3, **113 deps**) | S2 | NEW | 2026-03-17 |

**Timeline:** [2020096](https://bugzilla.mozilla.org/show_bug.cgi?id=2020096) (S2/P2) was filed 2026-02-28 and is blocked by the long-running blob rendering meta bug. Two fresh regressions ([2023989](https://bugzilla.mozilla.org/show_bug.cgi?id=2023989), [2022954](https://bugzilla.mozilla.org/show_bug.cgi?id=2022954)) were filed this week (Mar 12-17), suggesting active SVG regression churn in nightly builds. The blob rendering meta [1582153](https://bugzilla.mozilla.org/show_bug.cgi?id=1582153) has 113 deps and an S2 severity, indicating persistent long-tail performance debt.

**Stagnation callout:** [2020096](https://bugzilla.mozilla.org/show_bug.cgi?id=2020096) is S2/P2 and has had no resolution in 18 days since filing. While it has been actively commented on, no assignee is set. Monitor closely.

---

### Theme 3: WebRender GPU Compositing Glitches

**User-facing impact:** WebRender's compositor layer produces visible rendering artifacts in several scenarios: 3D transforms combined with opacity produce broken visual output; NVIDIA RTX 40-series cards trigger GPU texture corruption and memory leaks with CSS animations; macOS's Layer Compositor causes large UI regions (address bar, video frames) to glitch; and the alt+tab window preview is glitchy on Intel+Nvidia dual-GPU setups.

**Breadcrumb table:**

| Bug ID | Summary | Severity | Status | Last Changed | Assignee |
|--------|---------|----------|--------|-------------|---------|
| [2013967](https://bugzilla.mozilla.org/show_bug.cgi?id=2013967) | 3d transforms don't display correctly with opacity and rotation (regression, **stalled**) | S2 | ASSIGNED | 2026-03-10 | (assigned) |
| [2019679](https://bugzilla.mozilla.org/show_bug.cgi?id=2019679) | WebRender GPU texture corruption + memory leak on NVIDIA RTX 40 series | S2 | UNCONFIRMED | 2026-03-12 | — |
| [2020844](https://bugzilla.mozilla.org/show_bug.cgi?id=2020844) | macOS Layer Compositor: Large parts of UI glitch | S2, P2 | UNCONFIRMED | 2026-03-09 | — |
| [1744455](https://bugzilla.mozilla.org/show_bug.cgi?id=1744455) | Alt+tab window preview is glitchy (Intel+Nvidia, regression) | S3 | NEW | 2026-03-15 | — |
| [2023466](https://bugzilla.mozilla.org/show_bug.cgi?id=2023466) | Pop out window is faded / greyish cast | S3, P3 | UNCONFIRMED | 2026-03-16 | — |
| [1975517](https://bugzilla.mozilla.org/show_bug.cgi?id=1975517) | Apple TV trailer videos use only magenta and white colors with SW-WR (regression) | -- | NEW | 2026-03-13 | — |

**Timeline:** [2013967](https://bugzilla.mozilla.org/show_bug.cgi?id=2013967) was filed Feb 2 and carries both `regression` and `stalled` keywords at S2 — the most alarming combination. It is ASSIGNED but stalled, meaning someone owns it but is blocked. [2019679](https://bugzilla.mozilla.org/show_bug.cgi?id=2019679) specifically calls out NVIDIA RTX 40-series GPUs, which represent a large and growing install base. [2020844](https://bugzilla.mozilla.org/show_bug.cgi?id=2020844) affects macOS and is UNCONFIRMED but has S2/P2.

**Stagnation callout:** [2013967](https://bugzilla.mozilla.org/show_bug.cgi?id=2013967) is S2, regression, stalled — last changed 2026-03-10 (< 30 days, barely). Marked as stalled with no resolution. Needs engineering attention.

---

### Theme 4: WebGL and Canvas Security and Stability

**User-facing impact:** A privacy-impacting bug allows Canvas to display on-screen content from *other running applications* on Linux systems using NVIDIA drivers with the dmabuf path. This is a potential information disclosure. Separately, WebGL stability issues cause Google Maps to go black and prevent valid WebGL2 shaders from linking on Windows.

**Breadcrumb table:**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2020195](https://bugzilla.mozilla.org/show_bug.cgi?id=2020195) | Canvas displays screen content from other apps via NVIDIA/dmabuf (**sec-vector**, reporter-external) | S2, P2 | UNCONFIRMED | 2026-03-15 |
| [2010645](https://bugzilla.mozilla.org/show_bug.cgi?id=2010645) | WebGL Google map turns black after zooming in and out | S3 | UNCONFIRMED | 2026-02-16 |
| [2019155](https://bugzilla.mozilla.org/show_bug.cgi?id=2019155) | Valid WebGL2 shaders get link error on Windows only | S3 | UNCONFIRMED | 2026-02-27 |
| [2015955](https://bugzilla.mozilla.org/show_bug.cgi?id=2015955) | Large event jank from synchronous image decoding in Kotlin-wasm | S3 | NEW | 2026-02-19 |
| [2018404](https://bugzilla.mozilla.org/show_bug.cgi?id=2018404) | webgl: report INVALID_ENUM instead of INVALID_VALUE for OOB activeTexture | S3 | UNCONFIRMED | 2026-02-23 |

**Timeline:** [2020195](https://bugzilla.mozilla.org/show_bug.cgi?id=2020195) was filed 2026-03-01 by an external reporter and tagged `sec-vector` — it should be prioritized for security triage. It is currently UNCONFIRMED at S2/P2. The bug blocks the Graphics Triage Tracker meta [1632611](https://bugzilla.mozilla.org/show_bug.cgi?id=1632611).

**Stagnation callout:** [2020195](https://bugzilla.mozilla.org/show_bug.cgi?id=2020195) is a `sec-vector` bug that has been UNCONFIRMED for 17 days. Needs security triage attention.

---

### Theme 5: Text Rendering Quality and Emoji Regression

**User-facing impact:** On macOS with Lockdown Mode enabled, emoji characters fail to render entirely (rendering as blank). On Linux Nightly, font rendering is globally blurry. Text can appear blurry until text selection sharpens it. A 1px dark artifact line appears in full-page screenshots taken by extensions after a recent Firefox update.

**Breadcrumb table:**

| Bug ID | Summary | Severity | Status | Last Changed | Assignee |
|--------|---------|----------|--------|-------------|---------|
| [2005440](https://bugzilla.mozilla.org/show_bug.cgi?id=2005440) | [Regression] Emojis fail to render on macOS (aarch64) in Lockdown mode — Firefox 146.0 | S3, P3 | ASSIGNED | 2026-03-16 | cmarco@mozilla.com |
| [2016821](https://bugzilla.mozilla.org/show_bug.cgi?id=2016821) | Blurry text, which becomes sharp when selecting | S3 | NEW | 2026-03-10 | — |
| [2018463](https://bugzilla.mozilla.org/show_bug.cgi?id=2018463) | Firefox Nightly Linux font rendering is blurry | S3 | UNCONFIRMED | 2026-02-23 | — |
| [1985706](https://bugzilla.mozilla.org/show_bug.cgi?id=1985706) | Full-page screenshots show a 1px dark line after recent Firefox update (regressionwindow-wanted) | S3, P3 | NEW | 2026-03-16 | — |

**Timeline:** [2005440](https://bugzilla.mozilla.org/show_bug.cgi?id=2005440) has been open since Dec 2025 and has 27 comments — the most community engagement of any text bug in the seed. It is ASSIGNED (cmarco@mozilla.com) but not resolved. The `regressionwindow-wanted` on [1985706](https://bugzilla.mozilla.org/show_bug.cgi?id=1985706) means the regression range has not yet been identified after 7 months of filing (Aug 2025).

---

### Theme 6: WebRender Internal Crashes

**User-facing impact:** Firefox crashes in WebRender internals across several subsystems. The TileCacheInstance crash is newly rising and exclusive to Windows. A GPU buffer assertion crash has been observed with pernosco-collected data. Multiple MOZ_CRASH assertions in render_task.rs and Assertions.cpp trace to WebRender edge cases that are reproducible with testcases.

**Socorro data:**
- [webrender::tile_cache::TileCacheInstance::setup_compositor_surfaces_impl](https://crashes.mozilla.org/signatures?q=signature%3A%22webrender%3A%3Atile_cache%3A%3ATileCacheInstance%3A%3Asetup_compositor_surfaces_impl%22): **19 reports in 30d**, Windows, nightly + beta 149. **Trend: rising** (0 reports in prior 30d window — this crash did not exist before Feb 2026).
- gpu_buffer / render_task: 0 Socorro results (may be deduped under other signatures or too rare to surface).

**Breadcrumb table:**

| Bug ID | Summary | Severity | Status | Last Changed | Crash Volume (30d) |
|--------|---------|----------|--------|-------------|---------------------|
| [2013247](https://bugzilla.mozilla.org/show_bug.cgi?id=2013247) | Crash in [@ TileCacheInstance::setup_compositor_surfaces_impl] | S3 | NEW | 2026-02-12 | **19** (rising, Windows) |
| [2021972](https://bugzilla.mozilla.org/show_bug.cgi?id=2021972) | Hit MOZ_CRASH(ElementAt) at Assertions.cpp (regression, bugmon) | S3 | NEW | 2026-03-13 | — |
| [2016487](https://bugzilla.mozilla.org/show_bug.cgi?id=2016487) | Hit MOZ_CRASH(max_block_count) at gpu_buffer.rs:446 (crash, pernosco) | S3 | NEW | 2026-02-19 | — |
| [2008381](https://bugzilla.mozilla.org/show_bug.cgi?id=2008381) | Hit MOZ_CRASH(explicit panic) at render_task.rs:45 (regression) | S3 | NEW | 2026-02-26 | — |

**Timeline:** The TileCacheInstance crash ([2013247](https://bugzilla.mozilla.org/show_bug.cgi?id=2013247)) was filed Jan 29, and Socorro confirms it is a rising Windows crash appearing only in nightly and beta 149 builds. This warrants a Socorro crash investigation to pin the regression window. [2021972](https://bugzilla.mozilla.org/show_bug.cgi?id=2021972) has `bugmon` keyword, meaning automated bisection is in progress. The gpu_buffer crash ([2016487](https://bugzilla.mozilla.org/show_bug.cgi?id=2016487)) has pernosco data attached, which should facilitate debugging.

---

### Theme 7: Graphics Memory Leaks

**User-facing impact:** Firefox's GPU process accumulates memory over time, particularly when pages containing video or WebGL are loaded. Specific applications (Foundry Virtual Tabletop) trigger a reproducible spike. A long-lived meta bug tracks this class of issue across many reporters.

**Breadcrumb table:**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [1902566](https://bugzilla.mozilla.org/show_bug.cgi?id=1902566) | [meta] Graphics memory leaks (system and/or gpu) — P2, **18 deps** | S3, P2 | NEW | 2026-02-18 |
| [2019679](https://bugzilla.mozilla.org/show_bug.cgi?id=2019679) | WebRender GPU texture corruption + memory leak on NVIDIA RTX 40 series | S2 | UNCONFIRMED | 2026-03-12 |
| [2017580](https://bugzilla.mozilla.org/show_bug.cgi?id=2017580) | GPU process memory growth when Foundry Virtual Tabletop is launched | S3 | UNCONFIRMED | 2026-02-20 |
| [2013674](https://bugzilla.mozilla.org/show_bug.cgi?id=2013674) | memory leak (Graphics) | S3 | UNCONFIRMED | 2026-02-25 |
| [1965442](https://bugzilla.mozilla.org/show_bug.cgi?id=1965442) | Freezing on text input or pausing/playing a video (18 comments) | S3, P3 | UNCONFIRMED | 2026-03-17 |

**Timeline:** The meta [1902566](https://bugzilla.mozilla.org/show_bug.cgi?id=1902566) has been open since June 2024 at P2 with 18 tracked deps. Despite being P2, the meta last changed in February 2026. [2019679](https://bugzilla.mozilla.org/show_bug.cgi?id=2019679) is a dual-concern bug (visual corruption + memory leak) on NVIDIA RTX 40 series, a cutting-edge GPU that is becoming more widespread.

---

### Theme 8: FreeType Font Security and Stability

**User-facing impact:** FreeType, the font rasterization library used by Firefox on Linux, has several crash and DoS vectors reported by external security researchers. A deep composite glyph chain can exhaust the stack. A separate crash occurs during memory copy in font stream reading. An integer overflow in the shared-memory segment reader allows an attacker to trigger a release-assert crash. A shutdown hang in font loading code can cause Firefox to appear frozen on exit.

**Breadcrumb table:**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2021699](https://bugzilla.mozilla.org/show_bug.cgi?id=2021699) | Stack exhaustion in FreeType load_truetype_glyph() via deep composite glyph chain (**csectype-dos**, reporter-external) | S3 | NEW | 2026-03-12 |
| [2008637](https://bugzilla.mozilla.org/show_bug.cgi?id=2008637) | Integer overflow in ShmSegmentsReader → release-assert crash (**csectype-intoverflow**, reporter-external) | S3 | UNCONFIRMED | 2026-02-19 |
| [2015471](https://bugzilla.mozilla.org/show_bug.cgi?id=2015471) | Crash in [@ memcpy \| FT_Stream_ReadAt] | S3 | NEW | 2026-02-20 |
| [2019903](https://bugzilla.mozilla.org/show_bug.cgi?id=2019903) | shutdownhang FT_Stream_ReadULong — LoadCmapsRunnable keeps running | S3, P3 | NEW | 2026-03-08 |

**Timeline:** [2021699](https://bugzilla.mozilla.org/show_bug.cgi?id=2021699) and [2008637](https://bugzilla.mozilla.org/show_bug.cgi?id=2008637) were both filed by external reporters with security-relevant keywords (`csectype-dos`, `csectype-intoverflow`). Neither has been confirmed or assigned. Socorro returned 0 results for `load_truetype_glyph` and `FT_Stream_ReadAt` signatures, suggesting these are rare in the wild but the security classification warrants triage.

**Stagnation callout:** [2008637](https://bugzilla.mozilla.org/show_bug.cgi?id=2008637) is a reporter-external bug with `csectype-intoverflow` that has been UNCONFIRMED for 73 days (filed Jan 5). This is a security-class bug that needs acknowledgment.

---

### Theme 9: WebRender Performance Regressions

**User-facing impact:** Users on certain sites (Bing search, Speedometer3, GTA VI website) experience measurably worse rendering performance. Speedometer3 and Bing search show automated perf-alert regressions. Scrolling on WebGL-heavy sites like Rockstar's GTA VI page is noticeably stuttering compared to Chromium.

**Breadcrumb table:**

| Bug ID | Summary | Severity | Status | Last Changed |
|--------|---------|----------|--------|-------------|
| [2020981](https://bugzilla.mozilla.org/show_bug.cgi?id=2020981) | 39.23-4.23% bing-search FirstVisualChange regression on Feb 23 (perf-alert) | S3, P3 | NEW | 2026-03-17 |
| [2023900](https://bugzilla.mozilla.org/show_bug.cgi?id=2023900) | 8.66-2.51% speedometer3 regression on March 9 (perf-alert) | -- | ASSIGNED | 2026-03-18 |
| [2012337](https://bugzilla.mozilla.org/show_bug.cgi?id=2012337) | Severe scrolling lag and stuttering on Rockstar Games GTA VI website | S3 | NEW | 2026-02-12 |
| [2020192](https://bugzilla.mozilla.org/show_bug.cgi?id=2020192) | Frame rate is limited to the monitor with lowest FPS | S3, P3 | UNCONFIRMED | 2026-03-12 |

**Timeline:** Two active perf-alert regressions trace to WebRender changes in February and March 2026. [2023900](https://bugzilla.mozilla.org/show_bug.cgi?id=2023900) was just filed yesterday and is already ASSIGNED. [2020192](https://bugzilla.mozilla.org/show_bug.cgi?id=2020192) (multi-monitor FPS cap) represents a long-standing UX complaint for users with mixed-refresh-rate displays.

---

## Emerging Theme: Forced Colors / Accessibility Regression (Stalled S2)

**Flagged for attention — stagnation:**

[1975275](https://bugzilla.mozilla.org/show_bug.cgi?id=1975275) — **Find in page is invisible in forced colors mode** (S2, regression, stalled, `access` keyword, 17 comments) — last changed **2026-02-26** (> 20 days ago, approaching 30-day stagnation threshold). This is an S2 accessibility regression that has been open since July 2025 and carries both `regression` and `stalled`. Users relying on forced colors (high-contrast mode) cannot use Find in Page. Only has `stalled` set — no engineer currently working on it.

---

## Closing

### Ranked Signal Summary

| Rank | Theme | Breadcrumbs | Meta Bug | Top Severity | Notes |
|------|-------|-------------|----------|-------------|-------|
| 1 | backdrop-filter Correctness & Performance | 13+ | [1888025](https://bugzilla.mozilla.org/show_bug.cgi?id=1888025) (51 deps), [1888024](https://bugzilla.mozilla.org/show_bug.cgi?id=1888024) | S2 | Chronic, multi-year, still accumulating new bugs |
| 2 | SVG Rendering Regressions & Performance | 7 | [1582153](https://bugzilla.mozilla.org/show_bug.cgi?id=1582153) (113 deps) | S2 | Two fresh regressions this week; S2/P2 resource exhaustion open |
| 3 | WebRender GPU Compositing Glitches | 6 | — | S2 | S2 stalled regression (2013967); NVIDIA RTX 40 series affected |
| 4 | WebGL / Canvas Security & Stability | 5 | — | S2 | sec-vector UNCONFIRMED for 17 days; privacy concern |
| 5 | Text Rendering & Emoji Regression | 4 | — | S3 | Emoji regression ASSIGNED (27 comments); screenshot artifact |
| 6 | WebRender Internal Crashes | 4 | — | S3 | TileCacheInstance rising (19 reports, Windows, nightly) |
| 7 | Graphics Memory Leaks | 5 | [1902566](https://bugzilla.mozilla.org/show_bug.cgi?id=1902566) (18 deps) | S2 | P2 meta, NVIDIA RTX overlap with Theme 3 |
| 8 | FreeType Security & Stability | 4 | — | S3 | Two reporter-external sec bugs unconfirmed; one 73 days old |
| 9 | WebRender Performance Regressions | 4 | — | S3 | Two perf-alert regressions active; Speedometer3 newly ASSIGNED |
| — | Forced Colors Accessibility (Emerging) | 1 | — | S2 | S2 stalled, 8 months old, approaching stagnation |

---

### Resources Used

- **Bugzilla REST API:** 6 queries (Query A creation-time seed, Query B recently-changed seed, 3 batch dep/detail fetches, 2 keyword expansion searches)
- **Socorro CLI:** 5 signature searches (`TileCacheInstance`, `load_truetype_glyph`, `dri2_allocate_textures`, `FT_Stream_ReadAt`, `gpu_buffer`), 2 trend comparison queries
- **Cache:** Written fresh this session

### Suggestions for Improving this Skill

- **Security triage awareness:** Bugs with `reporter-external` + `csectype-*` keywords that are UNCONFIRMED for >30 days are a gap. The skill could add a dedicated "security-class unconfirmed" callout.
- **Assignee staleness:** When a bug is ASSIGNED and has `stalled`, the skill could surface the last comment author and date to help determine if the assignee is still active.
- **Socorro batch search:** The skill currently searches Socorro one signature at a time. A batched approach with a facet search on all crash-keyword bugs at once would be faster.
- **Duplicate detection:** Multiple bugs in this run overlap themes (e.g., 2019679 spans Themes 3 and 7). A cross-reference table in the report would help readers understand shared breadcrumbs.

---

*"The detective's job is not to explain the universe — only to show that the clues, when gathered patiently, do not lie."*

---

*Report generated: 2026-03-18 | Scope: graphics | wrangler-graphics-2026-03-18.md*
