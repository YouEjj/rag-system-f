from haystack.nodes import EmbeddingRetriever
from haystack.document_stores import InMemoryDocumentStore 


# Étape 1 : Indexation des documents
def index_documents(documents):
    """Indexe les documents en utilisant un Document Store en mémoire."""
    document_store = InMemoryDocumentStore(embedding_dim=384)

    # Embedding model pour créer les vecteurs
    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model="sentence-transformers/all-MiniLM-L6-v2" 
        #embedding_model="sentence-transformers/paraphrase-MiniLM-L6-v2" 
    )

    # Conversion des documents en format Haystack
    docs_to_index = [{"content": doc} for doc in documents]

    # Écriture des documents dans le document store
    document_store.write_documents(docs_to_index)

    # Mise à jour des embeddings pour les documents indexés
    document_store.update_embeddings(retriever)

    print(f"Nombre de documents indexés : {document_store.get_document_count()}")
    print(f"Nombre d'embeddings : {document_store.get_embedding_count()}")

    return document_store, retriever


# Étape 2 : Recherche dans les documents
def retrieve_documents(query, retriever, document_store, top_k=3):
    """Recherche les k documents les plus pertinents depuis ceux indexes."""
    retrieved_docs = retriever.retrieve(query=query, top_k=top_k)
    return [doc.content for doc in retrieved_docs]