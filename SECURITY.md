# Security Policy and Scope

This is a public **educational reference**, not a security product and not a hosted service.

## Supported security boundaries

The executable example only computes and prints a routing **suggestion**. It does not authenticate callers, grant capabilities, invoke models, execute tools, access files, or send network requests. Requests for capabilities outside the exact allowlist are denied, and selected high-impact capabilities return `approval_required` without performing the operation.

## Known limitations

- Status `ready` does not provide permission to execute.
- There is no identity provider, cryptographic approval, tenant isolation, network policy gateway, durable tamper-evident audit log, distributed state or recovery mechanism.
- The example does not defend against a caller who modifies the source or bypasses the router. Real enforcement must occur at independent tool boundaries.
- Tests verify example behavior; a passing CI workflow is not a penetration test, vulnerability assessment or certification.

## Reporting vulnerabilities

Please avoid putting API keys, real customer data or exploit details into public issues. Use GitHub's private vulnerability reporting feature if it is enabled for this repository, or contact the maintainers through a private authorized channel. Do not attack systems outside your ownership or written testing authorization.

Security changes require isolated reproduction, tests for denied operations, review of permissions and evidence that no restricted resources are disclosed.
