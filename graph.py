from langgraph.graph import StateGraph, START, END
from states.graph_state import GraphState
from states.state_getter import state_getter
from agents.planner_agent import PlannerAgent
from agents.selector_agent import SelectorAgent
from agents.reporter_agent import ReporterAgent
from tools.serper import get_serper_response
from tools.scraper import get_scraper_response

builder = StateGraph(GraphState)

builder.add_node(
    "planner",
    lambda state: PlannerAgent(state).invoke(
        user_question=state["user_question"],
        get_feedback=lambda: state_getter(state, "reviewer_latest")
    )
)

builder.add_node(
    "serper_tool",
    lambda state: get_serper_response(
        state=state,
        get_planner_response=lambda: state_getter(state, "planner_latest")
    )
)

builder.add_node(
    "selector",
    lambda state: SelectorAgent(state).invoke(
        user_question=state["user_question"],
        get_feedback=lambda: state_getter(state, "reviewer_latest"),
        get_serp=lambda: state_getter(state, "serper_latest"),
        get_prev_selections=lambda: state_getter(state, "selector_all")
    )
)

builder.add_node(
    "scraper_tool",
    lambda state: get_scraper_response(
        state=state,
        get_selector_response=lambda: state_getter(state, "selector_latest")
    )
)

builder.add_node(
    "reporter",
    lambda state: ReporterAgent(state).invoke(
        user_question=state["user_question"],
        get_feedback=lambda: state_getter(state, "reviewer_latest"),
        get_context=lambda: state_getter(state, "scraper_latest"),
        get_prev_reports=lambda: state_getter(state, "reporter_all")
    )
)

builder.add_edge(START, "planner")
builder.add_edge("planner", "serper_tool")
builder.add_edge("serper_tool", "selector")
builder.add_edge("selector", "scraper_tool")
builder.add_edge("scraper_tool", "reporter")
builder.add_edge("reporter", END)


graph = builder.compile()

# for event in graph.stream({"user_question": "What is the capital of France?"}):
#     print(event, "\n\n")

print(graph.invoke({"user_question": "What is the capital of France?"}))