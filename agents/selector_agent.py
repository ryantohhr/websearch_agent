from typing import TypedDict, List
from langchain_core.messages import HumanMessage, SystemMessage
from agents.base_agent import BaseAgent
from prompts.selector_prompt import selector_prompt_template
from utils.date import get_date

class SelectorAgent(BaseAgent):
    def invoke(self, user_question, prompt=selector_prompt_template, get_feedback=None, get_serp=None, get_prev_selections=None):
        reviewer_response = get_feedback()
        feedback = reviewer_response["feedback"] if reviewer_response else ""

        prev_selections = get_prev_selections()

        selector_prompt = prompt.format(
            serp=get_serp(),
            feedback=feedback,
            prev_selections=prev_selections,
            date=get_date()
        )

        messages = [
            SystemMessage(content=selector_prompt),
            HumanMessage(content=user_question)
        ]

        llm = self.get_llm()
        llm_with_structured_output = llm.with_structured_output(SelectorOutput)
        response = llm_with_structured_output.invoke(messages)

        self.update_state("selector_response", response)

        return self.state
    
class SelectorItems(TypedDict):
    title: str
    link: str
    snippet: str
    
class SelectorOutput(TypedDict):
    selected_items: List = []