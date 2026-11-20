# Undertow showcase

This repository demonstrates how Undertow reports a business rule change in a pull request. Its [workflow](.github/workflows/change-review.yml) uses the published [Undertow GitHub Action](https://github.com/alpercandemir/undertow/releases/tag/v0.2.0).

The [free-delivery change](https://github.com/alpercandemir/undertow-showcase/compare/main...codex/free-delivery-threshold) lowers the entry threshold from above $50 to $50 and above. At exactly $50, `qualifies_for_free_delivery` used to return `False` and now returns `True`.

Open the PR conversation for the Undertow comment, or open the workflow run for its Markdown and JSON report. The example uses the built-in source analysis with the GitHub Actions token. The report links to the changed line on each revision.
