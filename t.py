from app.summarizer import summarize

text = """
Artificial intelligence is transforming many industries.
Machine learning is a subset of artificial intelligence.
NLP allows machines to understand human language.
Text summarization is an important NLP task.
This project demonstrates extractive summarization.
"""

print(summarize(text, top_n=2))
