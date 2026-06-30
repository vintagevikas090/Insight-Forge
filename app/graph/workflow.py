from langgraph.graph import StateGraph, START, END

from app.graph.state import GraphState

from app.tools.data_profiler import profile_dataset
from app.tools.safe_executor import execute_code

from app.agents.planner_agent import planner_agent
from app.agents.code_gen_agent import code_gen_agent
from app.agents.visualization_agent import visualization_agent
from app.agents.insight_gen_agent import insight_gen_agent


def profile_node(state):
    return {"dataset_profile": profile_dataset(state["df"])}


def execution_node(state):
    # print("\n" + "=" * 50)
    # print(state["generated_code"])
    # print("=" * 50 + "\n")
    result = execute_code(state["generated_code"], state["df"])
    return {"execution_result": result}


def response_node(state):
    return {
        "final_response": {
            "result": state["execution_result"],
            "chart_config": state["chart_config"],
            "insight": state["insight"]
        }
    }


builder = StateGraph(GraphState)

builder.add_node("profile", profile_node)
builder.add_node("planner", planner_agent)
builder.add_node("code_gen", code_gen_agent)
builder.add_node("execute", execution_node)
builder.add_node("visualize", visualization_agent)
builder.add_node("insight", insight_gen_agent)
builder.add_node("response", response_node)


builder.add_edge(START, "profile")

builder.add_edge("profile", "planner")
builder.add_edge("planner", "code_gen")
builder.add_edge("code_gen", "execute")
builder.add_edge("execute", "visualize")
builder.add_edge("visualize", "insight")
builder.add_edge("insight", "response")

builder.add_edge("response", END)


graph = builder.compile()




# from langgraph.graph import StateGraph, START, END

# from app.graph.state import GraphState

# from app.tools.data_profiler import profile_dataset
# from app.tools.safe_executor import execute_code

# from app.agents.planner_agent import planner_agent
# from app.agents.code_gen_agent import code_gen_agent
# from app.agents.insight_gen_agent import insight_gen_agent


# def profile_node(state):
#     return {"dataset_profile": profile_dataset(state["df"])}


# def execution_node(state):
#     result = execute_code(state["generated_code"], state["df"])

#     return {"execution_result": result}


# def response_node(state):
#     return {
#         "final_response": {
#             "result": state["execution_result"],
#             "chart_type": state["analysis_plan"].get("chart_type"),
#             "insight": state["insight"]
#         }
#     }


# builder = StateGraph(GraphState)

# builder.add_node("profile", profile_node)
# builder.add_node("planner", planner_agent)
# builder.add_node("code_gen", code_gen_agent)
# builder.add_node("execute", execution_node)
# builder.add_node("insight", insight_gen_agent)
# builder.add_node("response", response_node)

# builder.add_edge(START, "profile")

# builder.add_edge("profile", "planner")
# builder.add_edge("planner", "code_gen")
# builder.add_edge("code_gen", "execute")
# builder.add_edge("execute", "insight")
# builder.add_edge("insight", "response")

# builder.add_edge("response", END)

# graph = builder.compile()