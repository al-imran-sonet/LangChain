from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model =ChatAnthropic(model='claude-sonnet-4-5-20250929')

result = model.invoke("what is the capital of bangladesh ?")
print(result)
print(result.content)  # show only the results



# OPENAI_API_KEY = 

# ANTHROPIC_API_KEY =

# GOOGLE_API_KEY= 


