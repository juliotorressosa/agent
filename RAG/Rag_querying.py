from langchain_chroma import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langsmth_tracer import tracer

tracer()


#RAG application
#Embedding model
embeddings = OllamaEmbeddings(
    model = "qwen3-embedding:4b"
)

#Vector database
vector_store = Chroma(
    collection_name = "beatles",
    persist_directory="/Users/stoch/agent/RAG/.chroma_db",
    embedding_function=embeddings
)

#Retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

#LLM model
llm = ChatOllama(
    model="gemma3",
    temperature=0.0
)

#prompt
template = """You are a helpful assistant for answering questions about the Beatles.
Use just the following context {context} to answer the question. 
If you don't know the answer, say you don't know and remind the user the purpose of this system is
to answer questions about the Beatles based on the provided context.
{question}
"""
prompt = ChatPromptTemplate.from_template(template)

#LCEL chain
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()
)

query = input("Enter your question about the Beatles: ")
while query.lower() != "exit":
    print(f"Querying Beatles RAG system with question: {query}\n")
    
    for chunk in rag_chain.stream(query):
        print(chunk, end="", flush=True)
    print("\n")
    
    query = input("Enter your question about the Beatles (or type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Thank you for using the Beatles RAG system. Come back soon!")