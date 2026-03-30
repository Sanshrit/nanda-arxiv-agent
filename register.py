from nanda_adapter import NANDA
import os
from dotenv import load_dotenv

load_dotenv()

def arxiv_agent_logic(message_text: str) -> str:
    """
    Simple wrapper so NANDA can call our agent.
    Message should be a research topic.
    """
    from arxiv_fetcher import fetch_arxiv_abstracts
    from enricher import enrich_abstract
    import json

    papers = fetch_arxiv_abstracts(message_text, max_results=2)
    enriched = [enrich_abstract(p) for p in papers]
    return json.dumps(enriched, indent=2)

def main():
    nanda = NANDA(arxiv_agent_logic)
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    domain = "sanshrit.xyz"
    nanda.start_server_api(anthropic_key, domain)

if __name__ == "__main__":
    main()
