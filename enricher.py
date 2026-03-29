import anthropic
import json
import os
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def enrich_abstract(paper: dict) -> dict:
    """
    Takes a paper dict with title, authors, abstract, url.
    Returns the same dict enriched with structured fields
    extracted by Claude.
    """
    prompt = f"""You are a research paper analyst. Extract structured information from this abstract.

Title: {paper['title']}
Abstract: {paper['abstract']}

Return ONLY a JSON object with exactly these fields:
{{
    "methods": ["list of methods or techniques used"],
    "datasets": ["list of datasets mentioned, or empty list if none"],
    "key_findings": ["list of 2-3 main findings or contributions"],
    "domain_tags": ["list of 2-4 domain tags e.g. NLP, computer vision, agent systems"],
    "one_line_summary": "one sentence summary of the paper"
}}

Return only the JSON. No explanation, no markdown, no code blocks."""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )


    raw = response.content[0].text.strip()

    # Strip markdown code blocks if Claude wrapped the response
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    if not raw:
        raise ValueError("Empty response from Claude")

    enrichment = json.loads(raw)

    return {**paper, **enrichment}


if __name__ == "__main__":
    test_paper = {
        "title": "Towards a Decentralized Internet of AI Agents",
        "authors": ["Alice Chen", "Bob Martinez"],
        "abstract": "We propose a framework for decentralized agent discovery using cryptographic identity verification. Our approach addresses the limitations of DNS-based systems for dynamic AI agent registration and capability assertion. We deliver sub-second revocation, schema-validated capability assertions, and privacy-preserving discovery across organizational boundaries.",
        "url": "https://arxiv.org/abs/2507.00001"
    }

    result = enrich_abstract(test_paper)
    print(json.dumps(result, indent=2))