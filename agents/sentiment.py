from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.prompts import PromptTemplate
from langchain.tools import tool, ToolRuntime
from langsmth_tracer import tracer

#load_dotenv()
tracer()


### TOOLS
@tool
def message_sentiment_analysis(message: str) -> str:
    """Analyzes the sentiment of a message and returns whether it is positive, negative, or neutral."""
    # Here you would implement your actual sentiment analysis logic.
    # For demonstration purposes, we'll return a dummy response.
    if "good" in message.lower():
        return "positive"
    elif "bad" in message.lower():
        return "negative"
    else:
        return "neutral"

@tool
def user_question():
    """Returns the user's question."""
    question = input("Please enter your question: ")
    return question

### CONTEXT (to be done)


sys_message = SystemMessage(content="""You are a contact center agent, expert in the Beatles.
    You have the following context {context}. You have to strictly answer the question based on the context, 
    if you don't know the answer, say you don't know.
    Answer the following question: {question}""")
ai_message = AIMessage(content="""Hello, I am here to help you with any questions about the Beatles. 
                       Please provide the context and your question.""")

human_message = HumanMessage(content="""{question}""")

messages = [sys_message]

llm = ChatOllama(
    model = "llama3.1",
    temperature = 0.5,
    max_tokens = 500,
    streaming = True,
    verbose = True,
)

#tools calling
tools = [
    message_sentiment_analysis,
    user_question
]

llm_with_tools = llm.bind_tools(tools)
print("Agent is thinking...")

ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)
print(ai_message.content) ## line added by codeassistant

if ai_message.tool_calls:
        for tool_call in ai_message.tool_calls:
            tool_map = {
                "user_question": user_question,
                "message_sentiment_analysis": message_sentiment_analysis
            }
            selected_tool = tool_map[tool_call["name"]]
            
            tool_output = selected_tool.invoke(**tool_call["args"])

            messages.append(ToolMessage(content=tool_output, tool_call_id=tool_call["id"]))

response = llm_with_tools.invoke(messages)
print(response.content)

print("Agent has finished processing the question.")
print(ai_message.content)