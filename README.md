# NIGHT / SHIFT — ticket-transfer fixture

## Review a pull request with Undertow

This showcase uses the released Undertow GitHub Action. Try the historical ticket-preview regression and correction from the Actions tab. [Walkthrough](CHANGE-REVIEW.md).

## Automated behavior review

The **Behavior case gallery** workflow adds [eight reviewable cases](CASE-GALLERY.md): two happy paths, five distinct business-rule violations and one compilation failure. Open its Actions summary to compare all results and read actual operation traces.

Every push and pull request runs **Behavior review**. Open the check's **Details** and read the Actions summary; no local setup or commands are required from the reviewer.

- **ticket-transfer-candidate** checks this repository's actual ticket implementation.
- **refund-retry-candidate** checks the added standalone `refund-service` component.
- **refund-retry-calibration** and **ticket-transfer-calibration** deliberately inject labeled defects into disposable copies, reproduce them, execute generated JUnit assertions, then run the same tests and full suites on corrections. Their green status confirms the demonstration machinery, not candidate correctness.

The summary shows the existing-suite comparison, reduced operations, expected/observed state, replay result and proposed Java test. Its evidence link includes logs, source identities, replay JSON and a ready-to-apply regression patch. Candidate violations fail the check; execution problems are shown as incomplete.

The engineer accepts or revises the rule, requests a fix, and decides whether to retain the proposed regression. An implementation agent applies accepted changes in the PR, and CI runs again. The automation never merges, approves business policy or writes source. Test adoption means a reviewed test retained in source and executed by subsequent CI, not a person manually copying a file.

This remains an owned, self-authored showcase. It demonstrates automation and additional coverage for specific fixtures, not independent detection accuracy or measured human time savings. The vendored runner in `tools/undertow` has a complete source hash manifest in `SOURCE.json`; it comes from an unreleased Undertow working snapshot. Existing ticket contracts and their workflow remain intact.


A chat app previews a ticket-transfer invitation before its recipient opens it. A preview must leave the ticket with its sender and the invitation usable. Only the named recipient can accept it.

This is a deliberately small, fictional event and in-memory Java model. It tests observable state transitions, without a real ticketing provider, authentication server, HTTP endpoint, or deployment. It is not a production ticket service.

Run with JDK 21 and Maven:

```sh
mvn --batch-mode --no-transfer-progress clean test
```

Two owner-declared contracts bind unchanged, exact JUnit methods. The dedicated public repository is `alpercandemir/undertow-showcase`; its `main` contains the approved contracts, tests, and workflow before either example PR. The broken PR deliberately accepts a transfer during preview. The correction changes preview copy without accepting it. Both remain open for demonstration; the broken change must not be merged.

`on: push` produces evidence for the actual branch head, avoiding a pull-request merge-ref/head mismatch. The workflow has read-only repository permissions, no provider or publishing credentials, pinned actions, a clean test invocation, and retained assertion failures. Repository maintainers control these fixture branches; this workflow is not an anonymous code runner.

The assertions are intentionally limited. A passing fixture does not establish real identity, concurrency, provider integration, or production safety. GitHub artifacts have finite retention; archived demo reports are historical observations, not a fresh evaluation of a moving PR.
