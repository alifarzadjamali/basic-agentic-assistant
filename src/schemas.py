"""Small typed records passed between the workflow's agents.

Keeping these records explicit is deliberate: learners can see exactly what each
agent receives and returns without needing to infer a hidden prompt or memory.
"""

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class VisualAnalysis:
    palette: list[str]
    color_confidence: float
    image_quality: float
    needs_caption: bool
    caption: str | None = None

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class KnowledgeAnalysis:
    base_color: str
    matches: list[str]
    style: str
    used_rules: bool
    retrieval_confidence: float
    evidence: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class CriticAssessment:
    completeness_score: float
    grounding_score: float
    needs_revision: bool
    feedback: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)
