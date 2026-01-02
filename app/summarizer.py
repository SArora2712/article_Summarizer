import nltk
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download('punkt')

def read_article(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def summarize(text, top_n=3):
    sentences = read_article(text)
    return sentences[:top_n]
