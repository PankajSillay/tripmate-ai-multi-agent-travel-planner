from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

# res = tavily_search("Best Hotels in India")

res = search_flights("Plan a 7 day japan trip from new delhi")
print(res)