import os
from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is not set in the .env file")


client = TavilyClient(api_key=TAVILY_API_KEY)


def tavily_search(query: str) -> list[dict]:
    """
    Search the web using Tavily and return structured results.
    """

    response = client.search(
        query=query,
        max_results=5,
        search_depth="advanced"
    )

    results = []

    for r in response.get("results", []):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        content = r.get("content", "").strip()

        # Limit content length
        if len(content) > 500:
            content = content[:500].rsplit(" ", 1)[0] + "..."

        results.append({
            "title": title,
            "url": url,
            "content": content
        })

    return results