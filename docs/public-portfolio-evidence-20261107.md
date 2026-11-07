# Public portfolio evidence matrix

**ARAZVERA TECHNOLOGIES | Evidence snapshot: 7 November 2026**

This file describes only the public source and verifiable GitHub checks in this repository. It is **not** evidence that a commercial, hosted, autonomous, or security-certified AERON system exists.

| Claim a reviewer can verify | Location | Evidence | Important limitation |
| --- | --- | --- | --- |
| Deterministic Python capability routing | `examples/agent_routing.py` | Runnable offline CLI | Routing suggestions do not execute tools or authorize real-world actions |
| Fail-closed handling of unknown domains/capabilities | `examples/agent_routing.py` and `tests/test_agent_routing.py` | Unit-test cases for forbidden and unknown inputs | This is not a deployed security boundary |
| Explicit human-approval-required outcome | Routing demo and unit tests | Sensitive action examples return `approval_required` with `executed=false` | No independent human approval system is implemented |
| Reproducible CI test command | `.github/workflows/python-tests.yml` | Python 3.10, 3.12 and 3.13 matrices | Successful checks do not certify operational reliability |
| Reference architecture and known limitations | `docs/reference-architecture.md`, `docs/runnable-demo.md` | Public documentation | Design notes are not deployed infrastructure |

## Verified CI record

- The latest observed run for main at the time of this review completed successfully on 5 November 2026, commit `afbcbb37771a36a2a8580c3f08ff553483aa618d`.
- Evidence: [Python quality gate run 41967545467](https://github.com/arazvera-technologies/agentic-ai-architecture-notes/actions/runs/41967545467).
- All test outcomes must be rechecked for any later commit or branch. A previous successful run does not prove a proposed change is correct.

## Run locally

Requires Python 3.10+; no external model or API:

```bash
python -m unittest discover -s tests -v
python -m examples.agent_routing --domain documentation --tool draft_document
python -m examples.agent_routing --domain security --tool contain_host
python -m examples.agent_routing --domain documentation --tool contain_host
```

## Permitted portfolio description

> ARAZVERA TECHNOLOGIES maintains a public, offline Python reference example for permission-aware specialist routing, including deterministic negative-path tests and a GitHub Actions test matrix.

## Claims that must **not** be made from this repository alone

- A deployed autonomous multi-agent system, a hosted AI inference API, a production permission gateway, or any proprietary trained model.
- Verified customer deliveries, production uptime, security certification, benchmark superiority, or externally measured reliability.
- Working n8n integrations, commercial message delivery, multi-tenant isolation, or production Docker orchestration.

## Next independent acceptance gates

1. Keep any customer-neutral reusable engineering kits in a **separate private repository**. Do not copy private AERON runtime sources into this public repo.
2. For a new FastAPI portfolio demonstration, prove input validation, authentication, idempotency, negative paths and isolated integration tests before merging any sanitized sample.
3. For n8n, distinguish JSON structure checks from a full isolated n8n webhook execution and retry/recovery test.
4. For external model APIs, separately document pricing, privacy, rate limiting, timeout behavior, and measured test receipts.
5. Review the entire branch diff for secrets, personal/customer data, origin and license before approving publication.

**Publication gate:** Review-only draft; not an operational claim or a request to expose private company code.
