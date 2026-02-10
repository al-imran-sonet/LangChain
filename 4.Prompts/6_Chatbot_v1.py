# This is a simple chatbot that has no memory of previous conversation 
# For this reason ,If we talk something about thye previous query , it will not able to understand 


from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv

load_dotenv()

model =ChatPerplexity(model= 'sonar-pro')

template=PromptTemplate(
    template="""
{user_input} . Make the answer very small and precise .
If you dont know about the answer, just say that I dont know the answer.

""",
input_variable=['user_input'],
validation_tamplate=True
)

while True:
    user=input("you :")
    user=user.strip()  # If we put speces before and after the exit it will cut it 
    if user=='exit':
        break
    prompt=template.invoke(       # Making the prompt combining both user input and the template 
        {'user_input':user}
    )
    result=model.invoke(prompt)
    print(f"AI : {result.content}")