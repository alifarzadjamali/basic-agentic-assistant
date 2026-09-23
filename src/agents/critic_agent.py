"""A transparent critic that evaluates the evidence, not generated prose."""

from src.schemas import CriticAssessment, KnowledgeAnalysis


class CriticAgent:
    def __init__(self):
        pass

    def evaluate(
        self, knowledge_output: KnowledgeAnalysis, user_text: str | None = None
    ) -> CriticAssessment:
        matches = knowledge_output.matches
        used_rules = knowledge_output.used_rules
        retrieval_confidence = knowledge_output.retrieval_confidence

        # --- Decision variables ---
        completeness = self._check_completeness(matches)
        grounding = self._check_grounding(used_rules, retrieval_confidence)
        needs_revision = self._decide_revision(completeness, grounding)

        if not used_rules:
            feedback = "Retrieve a local rule before answering."
        elif needs_revision:
            feedback = "The retrieved rule is incomplete; revise or report the limitation."
        else:
            feedback = "The recommendation has enough local evidence."
        return CriticAssessment(
            completeness_score=completeness,
            grounding_score=grounding,
            needs_revision=needs_revision,
            feedback=feedback,
        )

    def _check_completeness(self, matches):
        return min(len(matches) / 4, 1.0)

    def _check_grounding(self, used_rules, retrieval_confidence):
        if used_rules:
            return retrieval_confidence
        return 0.4

    def _decide_revision(self, completeness, grounding):
        if completeness < 0.5:
            return True
        if grounding < 0.5:
            return True
        return False
