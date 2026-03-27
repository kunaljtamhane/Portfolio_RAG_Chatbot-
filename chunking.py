from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_chunks(file_path):
    """Reads a text file and chops it into smaller pieces and overlapping chunks."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            text = file.read()

        # Initialize the text splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, #max characters in a chunk
            chunk_overlap=50, # The 'glue' that bleeds over between chunks
            length_function = len,
            separators=["\n\n", "\n", " ", ""]  # it tries to split here first
            )

        # Split the text into chunks
        chunks = text_splitter.split_text(text)
        return chunks
    
    except Exception as e:
        print(f"Failed : {e}")
        return []