def state_getter(state, key):
    match key:
        case "planner_all":
            return state.get("planner_response", [])
        case "planner_latest":
            if state.get("planner_response", []):
                return state.get("planner_response", [])[-1]
            else:
                return state.get("planner_response", [])

        case "selector_all":
            return state.get("selector_response", [])
        case "selector_latest":
            if state.get("selector_response", []):
                return state.get("selector_response", [])[-1]
            else:
                return state.get("selector_response", [])

        case "reporter_all":
            return state.get("reporter_response", [])
        case "reporter_latest":
            if state.get("reporter_response", []):
                return state.get("reporter_response", [])[-1]
            else:
                return state.get("reporter_response", [])

        case "reviewer_all":
            return state.get("reviewer_response", [])
        case "reviewer_latest":
            if state.get("reviewer_response"):
                return state.get("reviewer_response", [])[-1]
            else:
                return state.get("reviewer_response", [])

        case "router_all":
            return state.get("router_response", [])
        case "router_latest":
            if state.get("router_response", []):
                return state.get("router_response", [])[-1]
            else:
                return state.get("router_response", [])

        case "serper_all":
            return state.get("serper_response", [])
        case "serper_latest":
            if state.get("serper_response", []):
                return state.get("serper_response", [])[-1]
            else:
                return state.get("serper_response", [])

        case "scraper_all":
            return state.get("scraper_response", [])
        case "scraper_latest":
            if state.get("scraper_response", []):
                return state.get("scraper_response", [])[-1]
            else:
                return state.get("scraper_response", [])
