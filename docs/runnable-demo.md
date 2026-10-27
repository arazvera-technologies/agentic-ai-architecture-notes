# Runnable specialist-agent router (offline demo)

This educational, deterministic example is independent of private infrastructure.
It contains no credentials, customer data, external API calls, AI model calls,
or real tool execution.

## Quick start

Requires Python 3.10+ and no external dependencies.
From the repository root:

~~~bash
python -m examples.agent_routing --domain documentation --tool draft_document
python -m examples.agent_routing --domain security --tool scan_metadata
python -m examples.agent_routing --domain security --tool contain_host
python -m examples.agent_routing --domain engineering --tool deploy_change
python -m examples.agent_routing --domain documentation --tool contain_host
~~~

Test suite:

~~~bash
python -m unittest discover -s tests -v
~~~

## Contract

Call route_request(RoutingRequest(request_id, domain, tool)).
It returns an immutable RoutingDecision containing:
- request_id: caller correlation key (up to 128 characters)
- status: ready, approval_required, or denied
- agent: specialist identifier or None for unknown domain
- tool: requested tool name, never translated into a system command
- reason: auditable policy explanation
- executed: always false, even for ready outcomes

| Specialist | Capability | Status |
| --- | --- | --- |
| documentation | draft_document, summarize_local | ready |
| security | scan_metadata | ready |
| security | contain_host | approval_required |
| engineering | draft_design | ready |
| engineering | deploy_change | approval_required |
| unknown or disallowed | anything | denied |

## Safety and limitations

- This is a demonstration of a routing decision, not a real autonomous agent,
  an access-control system, a hosted API, or a production security control.
- The ready outcome is not authorization and does not call an external tool.
- Strings supplied by callers do not override the hard-coded allowlist.
- Sensitive actions stay pending; this demo has no path to bypass approval.
- Real deployments require authenticated identities, enforced gateway scopes,
  independent approvals, auditing, robust monitoring, evaluation and recovery.
- No commercial delivery, deployment or benchmark performance is claimed.

See the [reference architecture](reference-architecture.md) and
[evaluation checklist](evaluation-checklist.md).
