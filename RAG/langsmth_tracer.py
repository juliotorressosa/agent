#Loading and connecting to langsmith
import os
from dotenv import load_dotenv

def tracer():
    load_dotenv()
    
    langsmith_api_key = os.getenv('langsmith_api_key')
    langsmith_endpoint = os.getenv('LANGSMITH_ENDPOINT')
    langsmith_project = os.getenv('LANGSMITH_PROJECT')
    langsmithtracing = os.getenv('LANGSMITH_TRACING', 'false').lower() == 'true'
