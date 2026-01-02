import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def sentence_similarity_matrix(sentences):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(tfidf, tfidf)
    return similarity_matrix
