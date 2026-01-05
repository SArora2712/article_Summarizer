**#  Context-Aware Article Summarizer**

A smart NLP-based web application that generates different summaries of the same article based on the target audience — Student, Professional, Researcher, or General.

Unlike standard summarizers, this system adapts language depth, sentence selection, and focus according to the reader.

###   Why This Project Matters

Most summarization tools generate a single generic summary.
This project demonstrates context-aware NLP, showing how summaries can adapt to the reader’s background:
    Audience-aware sentence selection
    Practical use of TextRank (graph-based ranking)
    Modular architecture separating NLP, audience logic, file handling, and UI
    Production-style features like file upload, visualization, and PDF export

# Supported Audiences
**Student**: Simple language, definitions,learning-focused
**Professional**: Concise, insight-driven, decision-oriented
**Researcher**: Technical, information-dense, keyword-heavy
**General**:	Balanced, neutral, easy-to-read
Each audience receives a different summary from the same article.

# Features
    Extractive summarization using TextRank
    Audience-specific sentence selection
    Adjustable summary length
    Handles long articles (≤ 2000 words recommended)
    Clear bullet-pointed summaries
    Input Support
    Paste raw text
    Upload TXT, PDF, or DOCX files
    Visualization & Export
    Word cloud visualization
    Multiple display modes:
    Summary only
    Word Cloud only
    Summary + Word Cloud
    Export generated summary as PDF (summary + Word Cloud together)

# How It Works
    Text Extraction – Reads text from file or text area
    Sentence Tokenization – NLTK splits content into sentences
    Vectorization – TF-IDF vectors for sentences
    Similarity Graph – Cosine similarity + NetworkX graph
    TextRank Scoring – PageRank for sentence importance
    Audience-Aware Selection – Chooses sentences tailored to target audience
    UI Rendering – Streamlit frontend with export and visualization

# Tech Stack
    Python 3.13
    NLTK
    Scikit-learn
    NetworkX
    Streamlit
    WordCloud
    PyPDF2
    python-docx
    ReportLab

# Setup & Run Instructions
    # Clone the repo
    git clone <your-repo-url>
    cd <your-project-folder>

    # Create a virtual environment
    python -m venv venv
    # Activate it
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt

    # Run the Streamlit app
    streamlit run app.py

# Future Enhancements
    Abstractive summarization (T5 / BART)
    Readability scoring per audience
    Side-by-side audience comparison
    Highlight factual vs analytical sentences

# Use Cases
    Educational platforms
    Research assistants
    Business insights summarization
    Knowledge management tools
    Portfolio / resume-grade NLP demonstration

