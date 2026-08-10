from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# res = tavily_search("Best Hotels in India")
# print(res)

# res = search_flights("Plan a 7 day japan trip from new delhi")
# print(res)

user_input = input("Enter travel requests : ")
response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)
print("\n Final Response: \n")
print(response["answer"])

