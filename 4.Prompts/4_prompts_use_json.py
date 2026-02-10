# Dynamic prompt

from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate , load_prompt
import streamlit as st 


load_dotenv()
model = ChatPerplexity(model="sonar-pro")

st.header("research Tool ")


# This is just streamelit dropdown menu creation code and from here we get the user input too 
paper_input= st.selectbox("Select Research Paper name ",["Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])
style_input=st.selectbox("Select writing style ",["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input= st.selectbox("Select length of summary ",["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])


# We will use the tamplate from json file

template=load_prompt('template.json') 


# we are using user input and the template and in combine this is a dynamic prompts 
prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
}
)

if st.button('Tell'):
    result=model.invoke(prompt)
    st.write(result.content)
