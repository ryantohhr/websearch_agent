def state_getter(state, key):
    match key:
        case "planner_latest":
            if state["planner_response"]:
                return state["planner_response"][-1]
            else:
                return state["planner_response"]

        case "reviewer_all":
            return state["reviewer_response"]
        case "reviewer_latest":
            if state["reviewer_response"]:
                return state["reviewer_response"][-1]
            else:
                return state["reviewer_response"]
