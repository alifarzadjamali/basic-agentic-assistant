# src/agents/orchestrator.py

from src.agents.critic_agent import CriticAgent
from src.agents.knowledge_agent import KnowledgeAgent
from src.agents.visual_agent import VisualAgent


class Orchestrator:
    def __init__(self):
        self.visual_agent = VisualAgent()
        self.knowledge_agent = KnowledgeAgent()
        self.critic_agent = CriticAgent()

    def run(self, image, image_path=None, user_text=None):
        state = {
            "user_text": user_text,
            "revision_count": 0,
            "max_revisions": 1
        }

        visual_output = self.visual_agent.analyze(
            image,
            image_path=image_path
        )

        state["visual_output"] = visual_output

        knowledge_output = self.knowledge_agent.analyze(
            visual_output,
            user_text
        )

        state["knowledge_output"] = knowledge_output

        critic_output = self.critic_agent.evaluate(
            knowledge_output,
            user_text
        )

        state["critic_output"] = critic_output

        while (
            critic_output["needs_revision"]
            and state["revision_count"] < state["max_revisions"]
        ):
            state["revision_count"] += 1

            visual_output["color_confidence"] = 0.3

            knowledge_output = self.knowledge_agent.analyze(
                visual_output,
                user_text
            )

            critic_output = self.critic_agent.evaluate(
                knowledge_output,
                user_text
            )

            state["knowledge_output"] = knowledge_output
            state["critic_output"] = critic_output

        return state
