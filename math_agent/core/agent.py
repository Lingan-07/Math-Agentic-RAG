import asyncio
from core.knowledge_base import search_kb
from core.web_search import web_search

async def math_agent_route(query: str) -> str:

    kb_answer = search_kb(query)
    if kb_answer:
        return f"📚 From Knowledge Base:\n {kb_answer}"
    
    web_result = web_search(query)
    if "No relevant information" not in web_result:
        return f"🌐 From Web Search:\n{web_result}\n\n(Summarized from educational sources.)"
    
    return "🤖 I could not find this in my KB or online sources."