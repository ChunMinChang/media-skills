

**todo**

- Define a default date range (last three months)

- cc_count enrichment: The seed fetch did not return cc_count in the API response despite requesting it. A follow-up targeted fetch step would improve signal scoring accuracy.

- Interop meta-bug deduplication: The seed window was heavily skewed by a single-day burst of Interop 2026 child bugs. Consider filtering out bugs that are child-of a known meta-bug when computing the "user-facing vs. infrastructure" ratio of the seed.

- Site-specific WebRTC bugs: The webcompat:site-report keyword search returned zero results for this scope. This may be because site-report bugs for WebRTC are filed under a different product (e.g., Web Compatibility). Worth adding a cross-product site-report search in a future iteration.


 Site Reports Resolution: --- Product: Web Compatibility - high value data?