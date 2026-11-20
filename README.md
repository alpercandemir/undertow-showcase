# Undertow showcase

This repository demonstrates how Undertow reports a business rule change in a pull request. Its [workflow](.github/workflows/change-review.yml) uses the published [Undertow GitHub Action](https://github.com/alpercandemir/undertow/releases/tag/v0.2.1).

In the [free-delivery example PR](https://github.com/alpercandemir/undertow-showcase/pull/5), orders of exactly $50 become eligible for free delivery. Only the eligibility function changes. The standard checkout uses it to calculate shipping, and gift checkout uses that same shipping calculation. Both callers stay outside the diff.

Open the PR conversation for the Undertow comment and the source references linking these flows. The workflow also publishes Markdown and JSON reports. This example uses the built-in source analysis with the GitHub Actions token.
