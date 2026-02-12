from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
from langchain_core.prompts import PromptTemplate


llm= HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 128,
        "temperature": 0.7,
    }
)
model =ChatHuggingFace(llm=llm)



# 1st prompt
temp1=PromptTemplate(
    template="write a detailed on {topic}",
    input_variables=["topic"]


)


# 2nd promt 

temp2=PromptTemplate(
    template="write a 5 line summery on folowing text ./n {text}",
    input_variables=["text"]


)

prompt1=temp1.invoke({"topic":'black hole '})

result= model.invoke(prompt1)

prompt2=temp2.invoke({'text':result})

result2= model.invoke(prompt2)

#print(result)
print(result2)




