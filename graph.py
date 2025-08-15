from langgraph.graph import StateGraph, START, END
from states.graph_state import GraphState
from states.state_getter import state_getter
from agents.planner_agent import PlannerAgent
from agents.selector_agent import SelectorAgent
from agents.reporter_agent import ReporterAgent
from agents.reviewer_agent import ReviewerAgent
from tools.serper import get_serper_response
from tools.scraper import get_scraper_response

def build_graph():
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

    builder.add_node(
        "reviewer",
        lambda state: ReviewerAgent(state).invoke(
            user_question=state["user_question"],
            get_plan=lambda: state_getter(state, "planner_latest"),
            get_answer=lambda: state_getter(state, "reporter_latest"),
            get_context=lambda: state_getter(state, "scraper_latest"),
            get_prev_feedback=lambda: state_getter(state, "reviewer_all")
        )
    )

    def final_answer(state: GraphState):
        answer = state["reporter_response"][-1]["report"]

        print(f"Final answer:\n{answer}")

    builder.add_node(
        "final",
        lambda state: final_answer(state)
    )

    def router(state: GraphState):
        next_node = state["reviewer_response"][-1]["next_node"]
        
        return next_node



    builder.add_edge(START, "planner")
    builder.add_edge("planner", "serper_tool")
    builder.add_edge("serper_tool", "selector")
    builder.add_edge("selector", "scraper_tool")
    builder.add_edge("scraper_tool", "reporter")
    builder.add_edge("reporter", "reviewer")
    builder.add_conditional_edges(
        "reviewer", 
        lambda state: router(state)
    )
    builder.add_edge("final", END)

    graph = builder.compile()

    return graph
