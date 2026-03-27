from s3_utils import download_document
from s3_utils import upload_document
from chunking import get_chunks
from vector_store import create_vector_store
from retrieval import retrieve_context
from chatbot import generate_answer
# ------------------------------------Phase 1: Storage & Architecture (AWS S3) ------------------------------
# Uploading Document to the S3 Bucket 
# upload_document("Kunal_Tamhane_Resume.txt", "Kunal_Tamhane_Resume.txt")

# Downloading Document from the S3 Bucket
#download_document("Kunal_Tamhane_Resume.txt", "downloaded_resume.txt")

# ------------------------------------ Phase 2: Chunking the downloaded Data ---------------------------------

# my_chunks = get_chunks("downloaded_resume.txt")

# # Inspecting the first chunk to make sure it didnot cut the name in half
# if my_chunks:
#     print("\n --- THE FIRST CHUNK ----")
#     print(my_chunks[0])
#     print("---------------------------\n")

# ------------------------------------ Phase 3: The translators (Embeddings and Vector Storage) ---------------------------------
# #Get the chunks from the local file
# my_chunks = get_chunks("downloaded_resume.txt")

# # Turn them into vectors and save them to the database
# if my_chunks:
#     create_vector_store(my_chunks)

# ------------------------------------ Phase 4: The RAG magic (Retrieval + LLM) ---------------------------------
# Ask Test question that we know the answer to based on resume
question = "What university does Kunal attend and what is his major?"

# Fetch the chunks
found_chunks = retrieve_context(question)

# Print the results to see if the search engine works
if found_chunks:
    # print("\n Top Results Found:")
    # for i, chunk in enumerate(found_chunks):
    #     print(f"\n----Result {i+1} ----")
    #     print(chunk.page_content)
    final_answer = generate_answer(question, found_chunks)
    
    print("\n===============================")
    print("CHATBOT RESPONSE:")
    print("===============================\n")
    print(final_answer)
    print("\n===============================")