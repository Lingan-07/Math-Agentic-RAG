import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query: str) -> str:
    try:
        results = tavily.search(query=query, max_results=3)
        if not results or "results" not in results:
            return "No relevant information found online."

        summaries = []
        for r in results["results"]:
            summaries.append(f"- {r['title']}: {r['content'][:150]}...")

        return "\n".join(summaries)

    except Exception as e:
        return f"Web search failed: {e}"
