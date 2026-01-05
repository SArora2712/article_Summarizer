import nltk
import networkx as nx
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.audience import get_audience_summary

nltk.download('punkt')


def read_article(text):
    return nltk.sent_tokenize(text)


def sentence_similarity_matrix(sentences):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(sentences)
    sim_matrix = cosine_similarity(tfidf)
    np.fill_diagonal(sim_matrix, 0)
    return sim_matrix


def summarize(text, top_n=5, audience="student"):
    sentences = read_article(text)

    if len(sentences) == 0:
        return []

    sim_matrix = sentence_similarity_matrix(sentences)

    graph = nx.from_numpy_array(sim_matrix)
    scores = nx.pagerank(graph)

    # ✅ Build ranked_sentences PROPERLY
    ranked_sentences = sorted(
        [(sentences[i], scores[i]) for i in range(len(sentences))],
        key=lambda x: x[1],
        reverse=True
    )

    # ✅ Apply audience logic
    summary = get_audience_summary(
        ranked_sentences,
        audience=audience,
        top_n=top_n
    )

    return summary
