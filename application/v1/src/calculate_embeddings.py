"""
This files contains code for calculating embeddings with llms.
"""

import openai
from openai.embeddings_utils import get_embedding
from sklearn.metrics.pairwise import cosine_similarity


class Embeddings:
    def __init__(self, embedding='openai_embeddings', *args, **kwargs):
        self.embedding = getattr(self, embedding)
    
    def openai_embeddings(self, text):
        self.embedding = getattr(self, embedding)
        return get_embeddings(text)
    
    def huggingface_embeddings(self, text):
        pass 
    
    def text_compare(self, text1, text2, texts=None, *args, **kwargs):
        if texts is not None:
            pass 
        pass 
