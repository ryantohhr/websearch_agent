def state_getter(state, key):
    if key == "reviewer_all":
        return state["reviewer_response"]
    elif key == "reviewer_latest":
        if state["reviewer_response"]:
            return state["reviewer_response"][-1]
        else:
            return state["reviewer_response"]
