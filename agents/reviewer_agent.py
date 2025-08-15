from typing import TypedDict
from langchain_core.messages import HumanMessage, SystemMessage
from agents.base_agent import BaseAgent
from prompts.reviewer_prompt import reviewer_prompt_template
from utils.date import get_date


class ReviewerAgent(BaseAgent):
    def invoke(self, user_question, prompt=reviewer_prompt_template, get_plan=None, get_answer=None, get_context=None, get_prev_feedback=None):
        reviewer_all = get_prev_feedback()
        prev_feedback = []

        if reviewer_all:
            for response in reviewer_all:
                prev_feedback.append(response["feedback"])
        
        reviewer_prompt = prompt.format(
            answer=get_answer(),
            plan=get_plan(),
            context=get_context(),
            date=get_date(),
            prev_feedback=prev_feedback
        )

        messages = [
            SystemMessage(content=reviewer_prompt),
            HumanMessage(content=user_question)
        ]

        llm = self.get_llm()
        llm_with_structured_output = llm.with_structured_output(ReviewerOutput)
        response = llm_with_structured_output.invoke(messages)

        self.update_state("reviewer_response", response)

        return self.state

class ReviewerOutput(TypedDict):
    next_node: str
    feedback: str
    answer: str