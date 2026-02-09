from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Load environment variables from a .env file

llm=OpenAI(model='gpt-3.5-turbo-instruct') # Initialize the LLM with a specific model

result=llm.invoke("What is the capital of France?") # Invoke the LLM with a prompt