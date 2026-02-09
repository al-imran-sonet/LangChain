from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv() 

model= ChatOpenAI(model='gpt-4') # we can also pass some arguments like temperature, max_tokens etc.

# model= ChatOpenAI( Model='gpt-4', temperature=0.7,max_completions_tokens =10)   
# temperature is used to control the randomness(creativity) of the output. 
# Higher values like 0.8 will make the output more random, 
# while lower values like 0.2 will make it more focused and deterministic.
# max_completions_tokens is used to limit the length of the output. helps to controle cost.


result=model.invoke("what is the capital of bangladesh ?")

print(result) # show lots of things besides the results 
print(result.content)  # show only the results