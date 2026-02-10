# Dynamic prompt

from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st 


load_dotenv()
model = ChatPerplexity(model="sonar-pro")

st.header("research Tool ")


# This is just streamelit dropdown menu creation code and from here we get the user input too 
paper_input= st.selectbox("Select Research Paper name ",["Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])
style_input=st.selectbox("Select writing style ",["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])
length_input= st.selectbox("Select length of summary ",["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])


# We are making a template how the prompt will look like .
template= PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.    
""",
input_variables=['paper_input','style_input','length_input'],
validation_template=True
)


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
