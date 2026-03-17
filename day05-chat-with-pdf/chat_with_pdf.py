from openai import OpenAI
from pypdf import PdfReader
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

        return text
    
def chunk_text(text, size=500):
    chunks = []
    for i in range(0, len(text), size):
        chunks.append(text[i:i+size])
    return chunks

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def build_vector_store(chunks):
    embeddings = [get_embedding(chunk) for chunk in chunks]
    return embeddings

def find_best_chunk(question, chunks, embeddings):
    question_embedding = get_embedding(question)
    similarities = cosine_similarity(
        [question_embedding],
        embeddings
    )[0]
    best_index = np.argmax(similarities)
    return chunks[best_index]

def ask_ai(question, context):
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.responses.create(
        model="gpt-5.4",
        input=prompt
    )

    return response.output_text

print("Loading PDF...")

text = extract_text("document.pdf")

chunks = chunk_text(text)

embeddings = build_vector_store(chunks)

print("Ready! Ask questions about the PDF.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    context = find_best_chunk(question, chunks, embeddings)

    answer = ask_ai(question, context)

    print("\nAI:", answer)
    print()