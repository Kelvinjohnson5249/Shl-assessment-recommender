from SHL_Vector_Store import vector_store, SHLVectorStore
from embedding import embedding_manager, EmbeddingManager
from langchain_core.documents import Document
from typing import List
class RAGRetriever:
    """Retriever class to fetch relevant assessments from vector store"""
    def __init__(self, vector_store: SHLVectorStore, embedding_manager: EmbeddingManager, top_k: int =5):
        self.vector_store = vector_store
        self.embedding_manager = embedding_manager
        self.top_k = top_k

    def retrieve(self, query: str, k:int | None = None) -> List[Document]:
        """Retrieve relevant documents based on the query"""
        #generate embedding for the query
        query_embedding = self.embedding_manager.generate_embeddings([query])

        n_results = k if k is not None else self.top_k

        #query the vector store
        results = self.vector_store.collection.query(
            query_embeddings = query_embedding.tolist(),
            n_results = n_results
        )

        retrieved_docs = []
        for doc_text, metadata in zip(results['documents'][0], results['metadatas'][0]):
            retrieved_docs.append(
                Document(
                    page_content = doc_text,
                    metadata = metadata
                )
            )
        return retrieved_docs
rag_retriever = RAGRetriever(vector_store, embedding_manager, top_k=5)
rag_retriever

def recommend_assessments(query: str, top_k: int = 10):
    docs = rag_retriever.retrieve(query, k=50)

    recommendations = []
    for doc in docs[:top_k]:
        recommendations.append({
            "assessment_name": doc.metadata.get("assessment_name", ""),
            "test_type": doc.metadata.get("test_type", ""),
            "url": doc.metadata.get("url", "")
        })


    return recommendations

def can_url(url: str):
    if not isinstance(url, str):
        return None
    url = url.strip().rstrip("/")
    url = url.replace("/solutions/products/","/products/")
    return url