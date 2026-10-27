# Reference architecture

The patterns below are general engineering examples, not a description or publication of any private internal system.

## System boundaries

1. **Ingress**: requests are authenticated, validated and assigned an idempotency key.
2. **Coordinator**: routes work by capability, capacity and explicit policy.
3. **Specialists**: handle a narrow domain with bounded context and approved tools.
4. **Tool gateway**: enforces permission scopes, rate limits, budgets and audit events.
5. **State store**: maintains structured task lifecycle and encrypted references where needed.
6. **Review gate**: checks high-impact writes or payments with an accountable human reviewer.
7. **Monitoring**: records latency, failures, queue depth, cost, retries and saturation.

## Minimal task lifecycle

\`\`\`mermaid
flowchart TD
    A[Validated request] --> B[Capability router]
    B --> C[Specialist agent]
    C --> D{External action required?}
    D -->|No| E[Evaluated answer]
    D -->|Yes| F[Policy gateway]
    F --> G{Approval required?}
    G -->|Yes| H[Human review]
    G -->|No| I[Scoped tool execution]
    H -->|Approved| I
    H -->|Denied| J[Safe refusal or revision]
    I --> E
\`\`\`

## Reliability considerations
- Use bounded queues, backpressure and hard execution deadlines.
- Distinguish retries for safe idempotent reads from irreversible operations.
- Prefer least-privilege temporary access over unrestricted global tokens.
- Preserve reproducible logs, without collecting passwords or raw sensitive records.
- Keep an explicit circuit breaker for failed dependencies.

## Safety constraints
No high-impact action runs without policy evaluation. Security testing is limited to owned or explicitly authorized assets. Defensive containment must not become unauthorized retaliation.
