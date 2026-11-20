# Try Undertow on a ticket preview change

A chat app can open a ticket-transfer link to show a preview. Mira owns the ticket until Leo accepts. The historical regression called `accept` while building that preview and transferred ownership before Leo acted.

1. Open **Actions → Undertow change review → Run workflow**.
2. Choose **regression**. Open the run summary. The unchanged JUnit test should pass three times on the base and fail at the same ownership assertion three times on the candidate. It will report that the owner was Leo where it expected Mira.
3. Run again with **correction**. The same ownership test should pass on both commits. The preview wording is outside that test's assertions.

| Scenario | Base | Candidate |
|---|---|---|
| Regression | `b73b50a` | `04b896b` |
| Correction | `b73b50a` | `59903f7` |

Open the **undertow-change-review** artifact for both commit IDs, selected tests, replay results, build logs and the source diff. The workflow also runs on normal pull requests, where the action selects the commits automatically.

This repository consumes the public Undertow action pinned to the exact commit for its release. Set `java-version` to your own project's JDK when installing it elsewhere. See the [release and portable CLI](https://github.com/alpercandemir/undertow/releases/tag/v0.1.1-alpha.1) and the [installation instructions](https://github.com/alpercandemir/undertow/blob/v0.1.1-alpha.1/docs/change-review.md).
