import time

def fetch_arxiv_abstracts(topic: str, max_results: int = 5) -> list[dict]:
    """
    Returns mock arXiv abstracts for local development.
    Swap this out for the real API call once arXiv is reachable.
    """
    time.sleep(1)  # simulate network delay

    mock_papers = [
        {
            "title": "Towards a Decentralized Internet of AI Agents",
            "authors": ["Alice Chen", "Bob Martinez"],
            "abstract": f"We propose a framework for decentralized agent discovery using cryptographic identity verification. Our approach addresses the limitations of DNS-based systems for dynamic AI agent registration and capability assertion in the context of {topic}.",
            "url": "https://arxiv.org/abs/2507.00001"
        },
        {
            "title": "AgentFacts: Verifiable Capability Assertions for Autonomous Systems",
            "authors": ["Carol Singh", "David Kim", "Eve Johnson"],
            "abstract": f"This paper introduces AgentFacts, a schema for cryptographically verifiable capability assertions in multi-agent systems. We demonstrate applications in {topic} with sub-second revocation and privacy-preserving discovery.",
            "url": "https://arxiv.org/abs/2507.00002"
        },
        {
            "title": "LLM-Powered ETL Pipelines for Research Paper Ingestion",
            "authors": ["Frank Liu", "Grace Patel"],
            "abstract": f"We present an end-to-end pipeline for ingesting and enriching research abstracts using large language models. The system extracts structured entities including methods, datasets, and findings from unstructured text in the domain of {topic}.",
            "url": "https://arxiv.org/abs/2507.00003"
        }
    ]

    return mock_papers[:max_results]


if __name__ == "__main__":
    results = fetch_arxiv_abstracts("agentic AI infrastructure", max_results=3)
    for paper in results:
        print(f"\nTitle: {paper['title']}")
        print(f"Authors: {', '.join(paper['authors'])}")
        print(f"URL: {paper['url']}")
        print(f"Abstract: {paper['abstract'][:200]}...")