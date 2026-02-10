# The task is we will get reviews , the code will take the review and take to the LLMs.

# LLMs will create structured output . The dictionary will contain summary and sentiment.
# we will use typedDict

# now the question is how llms understand that we have to find summary and sentiment ?
# The answer is when we are creating the typedDictionary it will create a system level prompt along with the given propmt 
# for this reason the key name is vary importent 

# Now another problem is, it is very easy to missundertand what we are looking for.
# For this we can add exta instruction called annotation 

# Ther is another problem that there is no data validation. 
# It means the LLMs can make mistake. It can give different answer from your desire one 


from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional ,Literal

load_dotenv()

model =ChatPerplexity(model='sonar-pro')

class review(TypedDict):
    key_thems:Annotated[list[str],'write down all key item discussed in review ']
    summary: Annotated[str,"A brief summary of the review"]
    sentiment: Annotated[Literal['pos','neg'],"return sentiment of the revied ether good or bad. stick only this two  "]
    pros: Annotated[Optional[list[str]],'write down all the pros inside the list ']
    cons: Annotated[Optional[list[str]],'write down all the cons inside the list ']


structured_model = model.with_structured_output(review)

result= structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result)  # result is a dictionary 
