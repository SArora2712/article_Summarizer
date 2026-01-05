import streamlit as st
from wordcloud import WordCloud
from app.summarizer import summarize
from app.file import extract_text
from app.pdf import generate_pdf

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Context-Aware Article Summarizer",
    layout="wide"
)

st.markdown(
    """
    <h2 style="text-align:center;">Context-Aware Article Summarizer</h2>
    <p style="text-align:center; color:gray;">
    One article · Four audiences · Different summaries
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# -------------------------------------------------
# Sidebar — Inputs
# -------------------------------------------------
with st.sidebar:
    st.header("Input")

    uploaded_file = st.file_uploader(
        "Upload TXT / PDF / DOCX",
        type=["txt", "pdf", "docx"]
    )

    article_text = st.text_area(
        "Or paste article text",
        height=220,
        help="Recommended limit: ≤ 2000 words"
    )

    st.caption("⚠️ Large context increases processing time")

    audience = st.selectbox(
        "Target Audience",
        ["student", "professional", "researcher", "general"]
    )

    top_n = st.slider(
        "Summary length (sentences)",
        min_value=3,
        max_value=10,
        value=5
    )

    display_mode = st.radio(
        "Display Mode",
        ["Summary Only", "Word Cloud Only", "Summary + Word Cloud"]
    )

    generate = st.button("Generate Summary")

# -------------------------------------------------
# Main Output
# -------------------------------------------------
if generate:
    if not uploaded_file and not article_text.strip():
        st.warning("Please upload a file or paste article text.")
    else:
        with st.spinner("Analyzing content..."):
            text = extract_text(uploaded_file) if uploaded_file else article_text
            summary = summarize(text, top_n=top_n, audience=audience)

        # Generate Word Cloud if needed
        wc_image = None
        if display_mode != "Summary Only":
            wc = WordCloud(
                width=400, height=300, background_color="white"
            ).generate(" ".join(summary))
            wc_image = wc.to_array()

        st.divider()
        st.subheader(f"{audience.capitalize()} Summary")

        col1, col2 = st.columns([2, 1])

        # ---------------- Summary ----------------
        with col1:
            if display_mode != "Word Cloud Only":
                for s in summary:
                    st.markdown(f"- {s}")  # bullet points

            # PDF Export including Word Cloud if needed
            pdf_path = generate_pdf(
                summary, audience, wordcloud_image=wc_image if display_mode=="Summary + Word Cloud" else None
            )
            with open(pdf_path, "rb") as f:
                st.download_button(
                    "📥 Export as PDF",
                    f,
                    file_name=f"{audience}_summary.pdf"
                )

            # Clear input after PDF download
            article_text = ""
            uploaded_file = None

        # ---------------- Word Cloud ----------------
        with col2:
            if display_mode != "Summary Only" and wc_image is not None:
                st.image(wc_image, use_container_width=True)
