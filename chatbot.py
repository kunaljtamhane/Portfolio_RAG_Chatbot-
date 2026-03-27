import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI

load_dotenv()
def generate_answer(user_question, retrieved_chunks):
    """Feeds the question and the retrieved chunks to gemini to get an final answer"""
    try:
        # Mash our3 retrieved chunks into one giant string of text
        context_text = "\n\n".join([chunk.page_content for chunk in retrieved_chunks])
        # Build the Master Prompt (The Guardrails!)
        prompt = f"""
        You are the professional AI assistant for Kunal Jatin Tamhane's portfolio website.
        Your job is to answer questions about Kunal using ONLY the context provided below.
        
        Rules:
        - If the answer is not in the context, say "I don't have that information."
        - Do not hallucinate or make up facts.
        - Keep your answer professional but conversational.
        
        Context:
        {context_text}
        
        User Question: {user_question}
        """
        #Spin up the Gemini Chat Model
        # We use gemini-1.5-flash because it's incredibly fast and perfect for RAG
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        
        print("Gemini is reading the context and thinking...")
        
        # 4. Send the prompt to the LLM
        response = llm.invoke(prompt)
        
        return response.content

    except Exception as e:
        print(f"Chatbot failed: {e}")
        return "Sorry, my brain is offline right now."