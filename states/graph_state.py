from typing import List, TypedDict, Annotated

class GraphState(TypedDict):
    user_question: str
    planner_response: List = []
    selector_response: List = []
    reporter_response: List = []
    reviewer_response: List = []
    router_response: List = []
    serper_response: List = []
    scraper_response: List = []
    final_answer: str