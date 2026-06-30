from app.graph.workflow import graph
from app.tools.chart_generator import generate_chart


class AnalystService:

    def analyze(self, df, question):
        state = {"question": question,"df": df}

        result = graph.invoke(state)
        response = result["final_response"]

        data = response["result"]
        chart = None

        if not data.empty:
            try:
                chart = generate_chart(data)
                # print("\nCHART:")
                # print(type(chart))

            except Exception:
                pass
            
        return {
            "data": data,
            "chart": chart,
            "insight": response["insight"]
        }


analyst_service = AnalystService()

