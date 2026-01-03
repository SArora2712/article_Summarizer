import nltk
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download('punkt')

def read_article(text):
    return nltk.sent_tokenize(text)

def sentence_similarity_matrix(sentences):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(sentences)
    sim_matrix = cosine_similarity(tfidf)
    np.fill_diagonal(sim_matrix, 0)
    return sim_matrix

def summarize(text, top_n=5, return_scores=False):
    sentences = read_article(text)
    sim_matrix = sentence_similarity_matrix(sentences)
    graph = nx.from_numpy_array(sim_matrix)
    scores = nx.pagerank(graph)

    ranked = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    if return_scores:
        return ranked[:top_n]
    return [s for _, s in ranked[:top_n]]
