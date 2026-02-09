from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv

load_dotenv()

model= ChatPerplexity(model='perplexity-chat-v1')

result= model.invoke("what is the capital of bangladesh ?")

print(result.content)