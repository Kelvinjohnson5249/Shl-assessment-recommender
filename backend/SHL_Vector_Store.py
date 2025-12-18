import os
import uuid
import numpy as np
import chromadb
from typing import Any, List




class SHLVectorStore:
    """Manages the embedded doc in a chromadb vector store"""
    def __init__(self, collection_name = "shl_assessments"):

        self.collection_name = collection_name
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.persist_directory = os.path.join(base_dir, "Vector_store_db")
        self.client = None
        self.collection = None
        self._initialize_store()
    def _initialize_store(self):
        """Intializing the chromadb client and collection"""
        try:
            os.makedirs(self.persist_directory, exist_ok = True)
            self.client = chromadb.PersistentClient(path = self.persist_directory)

            self.collection = self.client.get_or_create_collection(
                name = self.collection_name,
                metadata = {"Description": "SHL assessment docs for RAG"}
            )
            print(f"Vector stor initialized with collection: {self.collection_name}")
            print(f"Existing doc in collection: {self.collection.count()}")
        except Exception as e:
            print(f"Error initializing the vector store")
            raise
    def add_documents(self, documents: list[any], embeddings:np.ndarray):
        if len(documents)!= len(embeddings):
            raise ValueError("Number of docs and embeddings must match")

        print(f"Adding {len(documents)} to the vector store")
        
        ids = []
        metadatas = []
        document_text = []
        embedding_list = []

        for i, (doc, embedding) in enumerate(zip(documents, embeddings)):
            #unique id
            doc_id = f"doc_{uuid.uuid4().hex[:8]}_{i}"
            ids.append(doc_id)

            #preparing metadata
            metadata = {
                "assessment_name": doc.metadata.get("assessment_name", ""),
                "url": doc.metadata.get("url", ""),
                "test_type": doc.metadata.get("test_type", ""),
                "test_type_code": doc.metadata.get("test_type_code", ""),
                "doc_index": doc.metadata.get("doc_index", i),
                "content_length": doc.metadata.get("content_length", len(doc.page_content))
            }
            metadatas.append(metadata)

            #doc content
            document_text.append(doc.page_content)

            #embeddings
            embedding_list.append(embedding.tolist())

        #adding to collection
        try:
            self.collection.add(
                ids=ids,
                metadatas=metadatas,
                documents = document_text,
                embeddings = embedding_list
            )
            print(f"successfully added {len(documents)} documents.")
            print(f"Total document in collection: {self.collection.count()}")
        except Exception as e:
            print(f"Error adding doc to vector store")
            raise

vector_store = SHLVectorStore()
vector_store


