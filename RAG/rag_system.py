#RAG system using ollama qwen3-embedding:4b model
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
 
#Data ingestion. Opening a .pdf document
file_path = r"C:\Users\stoch\agent\RAG\Beatles.pdf"
loader = PyPDFLoader(file_path)
#Extract pages
pages = loader.load()
#Splitter
text_spliter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200,
    separators=["\n\n", "\n", " ", ""]
)
#Split the pages into smaller snippets
docs = text_spliter.split_documents(pages)
print(f"PDF loaded: {len(pages)} pages found.")
print(f"Created {len(docs)} chunks from the PDF.")

#Vector Storage. Chroma
####Embedding model
embeddings = OllamaEmbeddings(
    model = "qwen3-embedding:4b"
)
vector_db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=".chroma_db",
    collection_name="beatles"
)
print("Vector database created in .chroma_db")