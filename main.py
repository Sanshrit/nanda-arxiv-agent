from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from arxiv_fetcher import fetch_arxiv_abstracts
from enricher import enrich_abstract

app = FastAPI(
    title="NANDA arXiv Research Agent",
    description="Fetches and enriches arXiv abstracts using Claude AI",
    version="1.0.0"
)

class SearchRequest(BaseModel):
    topic: str
    max_results: int = 3

class SearchResponse(BaseModel):
    topic: str
    total: int
    papers: list[dict]

@app.get("/health")
def health_check():
    return {"status": "ok", "agent": "nanda-arxiv-agent"}

@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    if not request.topic.strip():
        raise HTTPException(status_code=400, detail="Topic cannot be empty")

    if request.max_results > 10:
        raise HTTPException(status_code=400, detail="max_results cannot exceed 10")

    papers = fetch_arxiv_abstracts(request.topic, request.max_results)

    enriched = []
    for paper in papers:
        enriched.append(enrich_abstract(paper))

    return SearchResponse(
        topic=request.topic,
        total=len(enriched),
        papers=enriched
    )