import os
from langsmth_tracer import tracer
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.tools import tool

tracer()

@tool
def even_numbers(number:int) -> str:
    """If the number is even returns the string "even". """
    if number % 2 == 0:
        return print("Even")
    else:
        return print("Odd")
    return
@tool
def multiply_numbers(x: float, y: float) -> float:
    """Multiplies the given numbers and returns the result."""
    result = x * y
    return result

llm = ChatOllama(
    model = "llama3.1",
    temperature = 0.0,
    max_tokens = 100,
    streaming = True,
    verbose = True,
)
tools = [even_numbers, multiply_numbers]
llm_with_tools = llm.bind_tools(tools)


messages = [
    SystemMessage(content=f"""You are a helpful assistant for determining if a number {number} is even or odd.
                  Use only the tools provided to determine if the number is even or odd. 
                  Do not provide an answer without using the tools.""")
    ]
    
response = llm_with_tools.invoke(f"is the number 112 even or odd?", messages=messages)
print(response.content)