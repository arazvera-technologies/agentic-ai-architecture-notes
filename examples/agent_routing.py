"""Permission-aware specialist routing demo.

This is an EDUCATIONAL SIMULATOR: no actions, API calls, or ML model invocations.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict, dataclass
import json


@dataclass(frozen=True)
class RoutingRequest:
    """Untrusted incoming task request."""
    request_id: str
    domain: str
    tool: str


@dataclass(frozen=True)
class RoutingDecision:
    """A routing suggestion, never a real-world permission token."""
    request_id: str
    status: str
    agent: str | None
    tool: str
    reason: str
    executed: bool = False


_CAPABILITIES = {
    "documentation": ("documentation_specialist",
                      {"draft_document": "read_only", "summarize_local": "read_only"}),
    "security": ("defensive_reviewer",
                 {"scan_metadata": "read_only", "contain_host": "approval_required"}),
    "engineering": ("software_architect",
                    {"draft_design": "read_only", "deploy_change": "approval_required"}),
}


def route_request(request: RoutingRequest) -> RoutingDecision:
    """Determine the specialist and status by exact allowlist, without execution."""
    if not isinstance(request, RoutingRequest):
        raise ValueError("request must be a RoutingRequest")
    if (not isinstance(request.request_id, str)
            or not 1 <= len(request.request_id) <= 128
            or request.request_id != request.request_id.strip()
            or not request.request_id.strip()):
        raise ValueError("request_id must be nonblank, trimmed, and <=128 characters")
    if not isinstance(request.domain, str) or not isinstance(request.tool, str):
        raise ValueError("domain and tool must be strings")

    definition = _CAPABILITIES.get(request.domain)
    if definition is None:
        return RoutingDecision(request.request_id, "denied", None, request.tool,
                               "Unknown domain; no fallback agent.")
    agent, permitted = definition
    level = permitted.get(request.tool)
    if level is None:
        return RoutingDecision(request.request_id, "denied", agent, request.tool,
                               "Capability not allowed for this specialist.")
    if level == "approval_required":
        return RoutingDecision(request.request_id, "approval_required", agent, request.tool,
                               "Requires independent human approval; no tool executed.")
    return RoutingDecision(request.request_id, "ready", agent, request.tool,
                           "Within specialist allowlist; simulated dispatch only.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline specialist-agent routing simulator")
    parser.add_argument("--request-id", default="demo-001")
    parser.add_argument("--domain", required=True,
                        help="documentation | security | engineering")
    parser.add_argument("--tool", required=True)
    args = parser.parse_args()
    decision = route_request(RoutingRequest(args.request_id, args.domain, args.tool))
    print(json.dumps(asdict(decision), indent=2))


if __name__ == "__main__":
    main()
