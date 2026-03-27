import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
# Load our secret keys from the .env file
load_dotenv()

def create_vector_store(chunks, save_path="faiss_index"):
    """Turns text chunks into vector embeddings and saves them locally."""
    try:
        print("Spinning up Gemini Embeddings.....")
        # Initialize the embedding model
        embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

        print(f"Converting {len(chunks)} chunks into math.....(this might take a few seconds)")
        # Build the FAISS index (The Vector Database)
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)

        # Save it locally so we don't have to re-embed every time we run the app
        vector_store.save_local(save_path)
        print(f"Vector store created and saved to {save_path}!")

    except Exception as e:
        print(f"Failed to create vector store: {e}")
