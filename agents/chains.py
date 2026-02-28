from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
#from langchain.tools import Tool

#load_dotenv()
#openai_apikey = os.getenv("openai_apikey")
#print(openai_apikey)

prompt = PromptTemplate(
    input_variables = ["question"],
    template = "What percentage of the Earth's surface is covered by water?"
)

llm = ChatOllama(
    model = "llama3.1",
    prompt = prompt,
    temperature = 1.0,
    max_tokens = 500,
    streaming = True,
    verbose = True,
)

#prompt = "What percentage of the Earth's surface is covered by water?"

response = llm.invoke(prompt)
print(response.content)
