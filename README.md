# Agentic AI Architecture Notes

**Public engineering reference | Offline educational demonstration, not a deployed product**

This repository demonstrates a narrow, testable aspect of specialist-agent systems: deterministic routing decisions based on explicit capability allowlists. It also documents broader architectural requirements for reliability, scoped tool use, auditing and human approval.

> The sample neither invokes an AI model nor executes an external tool. A `ready` decision is a simulation result, **not** an authorization to perform real-world actions.

## Run the working example

Requires Python **3.10+**, with no third-party Python dependencies.

```bash
git clone https://github.com/arazvera-technologies/agentic-ai-architecture-notes.git
cd agentic-ai-architecture-notes
python -m examples.agent_routing --domain documentation --tool draft_document
python -m examples.agent_routing --domain security --tool contain_host
python -m examples.agent_routing --domain engineering --tool deploy_change
python -m examples.agent_routing --domain documentation --tool contain_host
```

The CLI prints a JSON decision with a request identifier, routing status, suggested specialist, requested capability and human-readable reason. In **all** cases, `executed` is `false`.

## Run the tests

```bash
python -m unittest discover -s tests -v
python -m compileall -q examples tests
```

The test suite covers allowlisted capabilities, unknown domains/tools, cross-domain denial, required approvals, input validation, deterministic responses, and non-execution. GitHub Actions runs these checks for Python **3.10, 3.12 and 3.13** on changes to `main` and on pull requests.

**CI evidence:** [successful run from 5 November 2026](https://github.com/arazvera-technologies/agentic-ai-architecture-notes/actions/runs/41967545467) for commit `afbcbb37771a36a2a8580c3f08ff553483aa618d`. This is evidence for the listed test commands, **not** security certification or production suitability.

## Repository guide

| Path | Purpose |
| --- | --- |
| `examples/agent_routing.py` | Executable, no-side-effects routing example |
| `tests/test_agent_routing.py` | Deterministic positive and negative tests |
| `.github/workflows/python-tests.yml` | Automated Python checks |
| `docs/runnable-demo.md` | Demo contract and examples |
| `docs/reference-architecture.md` | Conceptual multi-agent boundaries |
| `docs/evaluation-checklist.md` | Suggested evaluation criteria |
| `docs/engineering-release-review-checklist.md` | Proposed pre-release review controls |
| `SECURITY.md` | Threat boundaries and disclosure guidance |
| `CONTRIBUTING.md` | Test and review expectations |

## Security and honest limitations

- No customer records, access keys, secret infrastructure details, or proprietary AERON runtime source are included.
- Policy entries are **illustrative**, not an enforceable IAM system.
- No authentication, approval token verification, live audit store, network gateway, resilience testing, or model evaluation is provided by this simulator.
- Any production gateway would require authenticated identities, enforced permission scopes, independent authorization, rate limits, telemetry, rollback and security review.
- No service-level objective, real deployment, paid engagement or model benchmark result is claimed.

This project is maintained as a professional, reproducible engineering reference by [ARAZVERA TECHNOLOGIES](https://github.com/arazvera-technologies). See [contribution guidance](CONTRIBUTING.md) before proposing changes.
