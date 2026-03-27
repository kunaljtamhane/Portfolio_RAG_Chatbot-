from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from retrieval import retrieve_context
from chatbot import generate_answer

# 1. Initialize the API app
app = FastAPI()

# 2. Add CORS Middleware
# This is CRITICAL. It tells your API, "It is safe to accept requests from Kunal's HTML file!"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For local testing, we allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Define the data structure we expect from the frontend
class ChatRequest(BaseModel):
    question: str

# 4. Create the actual API endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    print(f" Received question from frontend: {request.question}")
    
    try:
        # Step A: Retrieve the relevant chunks from FAISS
        found_chunks = retrieve_context(request.question)
        
        # Step B: Generate the answer using Gemini
        if found_chunks:
            bot_reply = generate_answer(request.question, found_chunks)
        else:
            bot_reply = "I couldn't find anything in Kunal's portfolio about that."
            
        return {"answer": bot_reply}
        
    except Exception as e:
        print(f" API Error: {e}")
        return {"answer": "Sorry, my backend brain had a glitch!"}