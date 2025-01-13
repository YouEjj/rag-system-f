import re
from text_manipulation import extract_text_from_pdf
from generator import generate_response
from retrieve import index_documents, retrieve_documents

if __name__ == "__main__":
    #pdf_path = "/content/PdfDataTest.pdf"
    pdf_path = "data/monopoly.pdf"

    # Extraire le texte du PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    # prise en charge des expressions regulière
    documents = re.split(r'(\d+\.)', pdf_text) 

    documents = [documents[i] + documents[i+1] for i in range(0, len(documents)-1, 2)]

    # Indexation des documents
    document_store, retriever = index_documents(documents)

query = "Explain the Speed Die rules in Monopoly."

retrieved_docs = retrieve_documents(query, retriever, document_store)

response = generate_response(query, retrieved_docs)
print(f"Generated response for query: '{query}'")
print(response)