# Contributing and Review Process

This repository is a small, dependency-free Python reference. Proposed changes must preserve its offline-only and non-executing nature.

## Before proposing a pull request

1. Describe the exact behavior being changed and why.
2. Add a failing behavioral test before implementing changes, where applicable.
3. Run `python -m unittest discover -s tests -v`.
4. Run `python -m compileall -q examples tests`.
5. Keep public examples synthetic, credential-free and independent of AERON proprietary code and customer environments.
6. Document whether the change affects authorization semantics or claimed capabilities.

Do not publish production credentials, customer messages, private network addresses, paid API examples, trading logic, private product implementations or fabricated benchmark results.

Merge/release approval is a separate human decision. Passing CI does not authorize unattended releases or operational permissions.
