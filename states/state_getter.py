def state_getter(state, key):
    match key:
        case "planner_all":
            return state["planner_response"]
        case "planner_latest":
            if state["planner_response"]:
                return state["planner_response"][-1]
            else:
                return state["planner_response"]

        case "selector_all":
            return state["selector_response"]
        case "selector_latest":
            if state["selector_response"]:
                return state["selector_response"][-1]
            else:
                return state["selector_response"]

        case "reporter_all":
            return state["reporter_response"]
        case "reporter_latest":
            if state["reporter_response"]:
                return state["reporter_response"][-1]
            else:
                return state["reporter_response"]

        case "reviewer_all":
            return state["reviewer_response"]
        case "reviewer_latest":
            if state["reviewer_response"]:
                return state["reviewer_response"][-1]
            else:
                return state["reviewer_response"]

        case "router_all":
            return state["router_response"]
        case "router_latest":
            if state["router_response"]:
                return state["router_response"][-1]
            else:
                return state["router_response"]

        case "serper_all":
            return state["serper_response"]
        case "serper_latest":
            if state["serper_response"]:
                return state["serper_response"][-1]
            else:
                return state["serper_response"]

        case "scraper_all":
            return state["scraper_response"]
        case "scraper_latest":
            if state["scraper_response"]:
                return state["scraper_response"][-1]
            else:
                return state["scraper_response"]
