# Static Prompt 

from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()
model =ChatPerplexity(model="sonar-pro")
st.header("Research Tool")

question=st.text_input("Enter your research question:") 

if st.button("Get Answer"):
    results =model.invoke(question)  
    st.write(results.content)



