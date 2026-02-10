from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage 

chat_template=ChatPromptTemplate([
    ("system","you are a helpfull {domain} expart"),
    ("human","Explain in simple terms, what is {topic}?")
]
)

prompt= chat_template.invoke({
    'domain':'cricket',
    'topic':'LBW'
})

print(prompt)