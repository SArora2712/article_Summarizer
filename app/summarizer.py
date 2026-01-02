import nltk
import networkx as nx
import numpy as np
from app.utils import sentence_similarity_matrix

nltk.download('punkt')

def read_article(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def summarize(text, top_n=3):
    sentences = read_article(text)

    if len(sentences) <= top_n:
        return sentences

    sim_matrix = sentence_similarity_matrix(sentences)

    graph = nx.from_numpy_array(sim_matrix)
    scores = nx.pagerank(graph)

    ranked_sentences = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)),
        reverse=True
    )

    summary = [s for _, s in ranked_sentences[:top_n]]
    return summary
