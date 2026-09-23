# Lesson 1: Inspect and extend an agentic workflow

**Goal:** understand why this is an agentic workflow rather than a single
function call.

## 1. Run it with a trace

```bash
uv run fashion-assistant --show-trace
```

For every trace entry, find the code that made that decision. Notice that each
entry identifies an agent, an action, and the evidence used.

## 2. Follow one state record

Open `src/schemas.py`. `VisualAnalysis` carries a palette and confidence into
the knowledge step. `KnowledgeAnalysis` adds a rule and its provenance. The
critic consumes that evidence rather than raw image pixels.

This is a useful design habit: give every agent a narrow responsibility and a
small, inspectable interface.

## 3. Make a safe change

Add a colour rule to `data/fashion_rules.json`. Then add a test asserting its
matches are returned by `find_best_match`. Run:

```bash
uv run pytest
```

## 4. Experiment with routing

In `KnowledgeAgent._decide_need_external`, alter the complexity threshold. Run
the same request before and after your change and compare `--show-trace` output.
Write down the trade-off: when did the workflow retrieve stronger evidence, and
when did it spend unnecessary work?

## Challenge

Replace the simple local rule matcher with a retrieval method that can explain
why it selected a rule. Keep the `KnowledgeAnalysis` provenance field and extend
the tests before connecting any language model.
