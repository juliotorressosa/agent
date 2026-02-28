import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import re 

#select the LLM you want to connect
print("Please select the LLM you want to connect to:")
print("1. Ollama")
print("2. OpenAI")
print("3. Anthropic")


tries = 1
while tries <= 3:
    choice = input("Enter your choice (1/2/3): ")
    try:
        match = re.match(r'^[1-3]$', choice)
        if not match:
            raise ValueError(f"Invalid choice. Please enter 1, 2, or 3. You have {3 - tries} tries left.")
        break
    except ValueError as e:
        print(e)
    tries += 1

load_dotenv()
if choice == "1":
    llm = ChatOllama
    print("Ollama selected")
    print("No API key needed for Ollama.")
elif choice == "2":
    llm = ChatOpenAI
    print("OpenAI selected")
    apikey = os.getenv("openai_apikey")
    print(f"Connecting to OpenAI with API key")
elif choice == "3":
    llm = ChatAnthropic
    print("Anthropic selected")
    apikey = os.getenv("anthropic_apikey")
    print(f"Connecting to Anthropic with API key")

