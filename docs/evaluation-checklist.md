# Evaluation checklist

Review a system on measured, repeatable behavior rather than agent count alone.

| Area | Minimum evidence |
| --- | --- |
| Correctness | Task-based evaluation suite and failure categorization |
| Concurrency | p50/p95 latency, queue depth, sustained throughput |
| Tool access | Least privilege, denied-action tests, audit samples |
| Reliability | Timeout, retry, degraded-mode and recovery tests |
| Human control | Approval flow for destructive writes and financial decisions |
| Security | Secret scans, input handling, dependency vulnerability review |
| Observability | Per-agent traces, resource measurements and error budgets |
| Cost | Limits for token usage, compute, storage and API calls |

A benchmark is credible only when the workload, environment, hardware, sample size and observed results are documented. No benchmark or commercial-performance claim is made by this reference repository.
