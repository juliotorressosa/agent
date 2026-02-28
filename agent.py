#Creating an agent model
from langchain import ChatOpenAI
from langchain import OpenAI
from langchain.agents.middleware import wrap_model_call,ModelRequest,ModelResponse
from langchain.tools import tool
from langchain.agents import create_agent


@wrap_model_call
def dynamic_model_selection(request:ModelRequest,handler) -> ModelResponse:
    """Choose a model based on converation context"""
    