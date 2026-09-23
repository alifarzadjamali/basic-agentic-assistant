# Contributing

Keep changes small, explicit, and useful to a learner. Prefer a clear rule and a
test over a hidden heuristic. Update the relevant lesson or README section when
you introduce a new concept.

Before opening a pull request, run:

```bash
uv run ruff check .
uv run pytest
```

Do not commit downloaded model weights, virtual environments, API keys, or
personal images without permission.
