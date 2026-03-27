import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

def retrieve_context(user_question):
    try:
        # we have to use the same embedding model we used to create the index
        embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
        # Load the database from your local folder
        vector_store = FAISS.load_local(
            "faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )

        #Perform the mathematical similarity search! Let's grab the Top 3 chunks.
        print(f"Searching Kunal's Database for: '{user_question}'.....")
        docs = vector_store.similarity_search(user_question, k=3)

        return docs
    
    except Exception as e:
        print(f"Failed to retrieve context: {e}")
        return []