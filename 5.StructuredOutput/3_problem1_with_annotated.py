# The task is we will get reviews , the code will take the review and take to the LLMs.
# LLMs will create structured output . The dictionary will contain summary and sentiment.
# we will use typedDict
# now the question is how llms understand that we have to find summary and sentiment ?
# The answer is when we are creating the typedDictionary it will create a system level prompt along with the given propmt 
# for this reason the key name is vary importent 
# Now another problem is, it is very easy to missundertand what we are looking for . for this we can add exta instruction called annotation 

from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model =ChatPerplexity(model='sonar-pro')

class review(TypedDict):
    summary: Annotated[str,"A brief summary of the review"]
    sentiment: Annotated[str,"return sentiment of the revied ether good or bad. stick only this two  "]

structured_model = model.with_structured_output(review)

result= structured_model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to
other brands. Hoping for a software update to fix this.
""")

print(result)  # result is a dictionary 
print(result['summary'])
print(result['sentiment'])  
