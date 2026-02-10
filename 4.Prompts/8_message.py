from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv

load_dotenv()
model= ChatPerplexity(model='sonar-pro')

messages=[
    SystemMessage(content='you are a helpful assistent'),
    HumanMessage(content='who are you ? ')
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)
