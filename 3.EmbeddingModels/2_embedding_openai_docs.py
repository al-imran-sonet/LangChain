from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

documents=[
    "bangladesh is a small country ",
    "paris is the capital of france ",
    "london is the capital of england "
]

vector=embedding.embed_documents(documents) # Embedding multiple documents
print(str(vector))