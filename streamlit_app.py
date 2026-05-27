import streamlit as st
from arxiv_fetcher import fetch_arxiv_abstracts
from enricher import enrich_abstract

st.set_page_config(
    page_title="arXiv Research Pipeline",
    page_icon="🔬",
    layout="centered"
)

st.title("🔬 arXiv Research Pipeline")
st.caption("Fetch and enrich the latest research papers for the topic of your choice")

topic = st.text_input("Research Topic", placeholder="e.g. multi-agent systems")
max_results = st.slider("Number of papers", min_value=1, max_value=5, value=3)

if st.button("Search", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic")
    else:
        with st.spinner("Fetching papers from arXiv..."):
            papers = fetch_arxiv_abstracts(topic, max_results)

        results = []
        for i, paper in enumerate(papers):
            with st.spinner(f"Enriching paper {i+1} of {len(papers)}..."):
                enriched = enrich_abstract(paper)
                results.append(enriched)

        st.success(f"Found and enriched {len(results)} papers")
        st.divider()

        for paper in results:
            st.subheader(paper["title"])
            st.caption(f"👥 {', '.join(paper['authors'][:3])}")
            st.write(f"**Summary:** {paper['one_line_summary']}")

            col1, col2 = st.columns(2)
            with col1:
                st.write("**Methods:**")
                for m in paper["methods"]:
                    st.write(f"- {m}")
            with col2:
                st.write("**Domain Tags:**")
                for t in paper["domain_tags"]:
                    st.write(f"- {t}")

            st.write("**Key Findings:**")
            for f in paper["key_findings"]:
                st.write(f"- {f}")

            st.link_button("View on arXiv →", paper["url"])
            st.divider()