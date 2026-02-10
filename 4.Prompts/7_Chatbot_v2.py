# In this chatbot we will include the memory of the to presurve the context of previous question 
# This is not perfect one . its just little update of previous one .
# in this there is a problem that in history we cant identify that is the user query and want is the AI's answer 

from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv

load_dotenv()

model =ChatPerplexity(model= 'sonar-pro')

chat_history=[]

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
    chat_history.append(user)
    result=model.invoke(prompt)
    chat_history.append(result)
    print(f"AI : {result.content}")

print(chat_history)