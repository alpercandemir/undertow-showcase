# Undertow showcase

Click #2934 introduced a regression that the existing test suite missed. A command iterating over stdin started aborting at normal end of input. This showcase uses a reviewed probe for that public API. Undertow generates the input, runs it on the two commits, and exports a pytest test using the original behavior as the expectation. [Original PR](https://github.com/pallets/click/pull/2934) · [Bug report](https://github.com/pallets/click/issues/2939)

| Check | Before the PR | With the PR | Upstream fix |
| --- | --- | --- | --- |
| Each revision's original pytest suite | 737 passed | 738 passed | 1,284 passed |
| Generated input of one stdin line | Exit 0 | `Aborted!`, exit 1 | Exit 0 |
| Generated pytest test | Pass | Fail | Pass |

Open the workflow in Actions and select **Run workflow**. The run summary shows the input and observed outputs. Download `click-stdin-regression` for the JSON evidence and generated test. The workflow compares the first two revisions. The evaluation includes the fixed revision and the original test suite runs. [Actions workflow](https://github.com/alpercandemir/undertow-showcase/actions/workflows/behavior-replay.yml) · [Workflow source](.github/workflows/behavior-replay.yml) · [Full Click evaluation](https://github.com/alpercandemir/undertow/blob/main/evaluation/click-replay.md)

The earlier storefront and coupon PRs illustrate known policy changes. The coupon PR already includes its own test for rounding the discount once per basket. [Storefront example](https://github.com/alpercandemir/undertow-showcase/pull/6) · [Coupon example](https://github.com/alpercandemir/undertow-showcase/pull/7)
