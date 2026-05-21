# import time

# def fetch_arxiv_abstracts(topic: str, max_results: int = 5) -> list[dict]:
#     """
#     Returns mock arXiv abstracts for local development.
#     Swap this out for the real API call once arXiv is reachable.
#     """
#     time.sleep(1)  # simulate network delay

#     mock_papers = [
#         {
#             "title": "Towards a Decentralized Internet of AI Agents",
#             "authors": ["Alice Chen", "Bob Martinez"],
#             "abstract": f"We propose a framework for decentralized agent discovery using cryptographic identity verification. Our approach addresses the limitations of DNS-based systems for dynamic AI agent registration and capability assertion in the context of {topic}.",
#             "url": "https://arxiv.org/abs/2507.00001"
#         },
#         {
#             "title": "AgentFacts: Verifiable Capability Assertions for Autonomous Systems",
#             "authors": ["Carol Singh", "David Kim", "Eve Johnson"],
#             "abstract": f"This paper introduces AgentFacts, a schema for cryptographically verifiable capability assertions in multi-agent systems. We demonstrate applications in {topic} with sub-second revocation and privacy-preserving discovery.",
#             "url": "https://arxiv.org/abs/2507.00002"
#         },
#         {
#             "title": "LLM-Powered ETL Pipelines for Research Paper Ingestion",
#             "authors": ["Frank Liu", "Grace Patel"],
#             "abstract": f"We present an end-to-end pipeline for ingesting and enriching research abstracts using large language models. The system extracts structured entities including methods, datasets, and findings from unstructured text in the domain of {topic}.",
#             "url": "https://arxiv.org/abs/2507.00003"
#         }
#     ]

#     return mock_papers[:max_results]


# if __name__ == "__main__":
#     results = fetch_arxiv_abstracts("agentic AI infrastructure", max_results=3)
#     for paper in results:
#         print(f"\nTitle: {paper['title']}")
#         print(f"Authors: {', '.join(paper['authors'])}")
#         print(f"URL: {paper['url']}")
#         print(f"Abstract: {paper['abstract'][:200]}...")

import requests
import xml.etree.ElementTree as ET
import time

def fetch_arxiv_abstracts(topic: str, max_results: int = 5) -> list[dict]:
    """
    Fetch latest abstracts from arXiv for a given topic.
    Returns a list of dicts with title, authors, abstract, url.
    """
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{topic}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }
    headers = {
        "User-Agent": "nanda-arxiv-agent/1.0 (bakshi.san@northeastern.edu)"
    }

    for attempt in range(3):
        wait = 5 * (attempt + 1)
        print(f"Attempt {attempt + 1} — waiting {wait}s...")
        time.sleep(wait)
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code == 200:
            break
        print(f"Got {response.status_code}, retrying...")
    else:
        raise Exception(f"arXiv API unavailable after 3 attempts")

    root = ET.fromstring(response.content)
    namespace = {"atom": "http://www.w3.org/2005/Atom"}

    papers = []
    for entry in root.findall("atom:entry", namespace):
        title = entry.find("atom:title", namespace).text.strip()
        abstract = entry.find("atom:summary", namespace).text.strip()
        url = entry.find("atom:id", namespace).text.strip()
        authors = [
            author.find("atom:name", namespace).text
            for author in entry.findall("atom:author", namespace)
        ]
        papers.append({
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "url": url
        })

    return papers


if __name__ == "__main__":
    results = fetch_arxiv_abstracts("multi-agent systems", max_results=2)
    for paper in results:
        print(f"\nTitle: {paper['title']}")
        print(f"Authors: {', '.join(paper['authors'][:3])}")
        print(f"URL: {paper['url']}")
        print(f"Abstract: {paper['abstract'][:200]}...")