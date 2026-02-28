import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate

#page config
st.set_page_config(page_title="Chat with Ollama", page_icon="💬")
st.title("Chat with Ollama")
st.markdown("This is an Ollma Gemma3 model chatbot.")

# Initialize the Ollama chat model
ollama_chat = ChatOllama(model="gemma3:latest",
                         temperature = 0.5)

# Define a prompt template
#prompt_template = PromptTemplate.from_messages(