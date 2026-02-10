# In this chatbot we will include the memory of the to presurve the context of previous question 
# This is not perfect one . its just little update of previous one .
# solve the problem of not able to identify user and AI's answer by using Message classes


from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import PromptTemplate 
from langchain_core.messages import SystemMessage, HumanMessage ,AIMessage
from dotenv import load_dotenv

load_dotenv()

model =ChatPerplexity(model= 'sonar-pro')

chat_history=[
    SystemMessage(content='You are my personal assistent ')
]

template=PromptTemplate(
    template="""
This is my previous chat history I stored {chat_history}. Now tell me {user_input} . Make the answer very small and precise .
If you dont know about the answer, just say that I dont know the answer.

""",
input_variable=['chat_history','user_input'],
validation_tamplate=True
)

while True:
    user=input("you :")
    user=user.strip()  # If we put speces before and after the exit it will cut it 
    
    if user=='exit':
        break
    prompt=template.invoke(       # Making the prompt combining both user input and the template 
        {'user_input':user,
         'chat_history':chat_history}
    )
    chat_history.append(HumanMessage(content=user))
    result=model.invoke(prompt)
    chat_history.append(AIMessage(content=result.content))
    print(f"AI : {result.content}")

print(chat_history)