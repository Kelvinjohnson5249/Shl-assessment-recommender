import numpy as np
from sentence_transformers import SentenceTransformer
from chromadb.config import Settings
import chromadb
from sklearn.metrics.pairwise import cosine_similarity
class EmbeddingManager:
    """This class will handle the embedding of docs"""
    def __init__(self, model_name: str = 'all-miniLM-L6-v2'):
        self.model_name = model_name
        self.model = None
        self._load_model()

    def _load_model(self):
        """loading the sentence transformers model"""
        try:
            print(f"loading Embedding model: {self.model_name}")
            self.model = SentenceTransformer(self.model_name)
            print(f"Model loaded successfully: Embedding dimensions: {self.model.get_sentence_embedding_dimension()}")
        except Exception as e:
            print(f"Error loading model: {self.model_name}: {e}")
            raise

    def generate_embeddings(self, texts: list[str])->np.ndarray:
        """generating embedding for the docs
        input is list
        output will be numpy array of embedding with shape(len(texts), embedding_dim)"""

        if not self.model:
            raise ValueError("Model not found")
        else:
            print(f"Generating for {len(texts)} texts")
            embeddings = self.model.encode(texts, show_progress_bar = True)
            print(f"Generated embedding with shape: {embeddings.shape}")
            return embeddings

#Initializing the embedding manager
embedding_manager = EmbeddingManager()
embedding_manager



