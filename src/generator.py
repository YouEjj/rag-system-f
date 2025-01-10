from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


# Étape 3 : Génération avec Hugging Face
def generate_response(query, retrieved_docs):
    """Génère une réponse à partir des documents récupérés."""

    model_name = "google/flan-t5-large"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    context = " ".join(retrieved_docs)
    #prompt = f"Generate your own detailed response to the question:\nQuestion: {query} \nResponse:"
    prompt = f"Answer the following question using the given context, in a detailed manner:\n{context}\n\nQuestion: {query}\nResponse:"
    #prompt = f"Given the following information, please provide a detailed answer, adding any relevant information you know:\n{context}\n\nQuestion: {query}\nResponse:"

    # Générer une réponse
    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(**inputs, max_length=300)
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",retrieved_docs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)