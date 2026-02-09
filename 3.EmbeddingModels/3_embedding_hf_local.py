from langchain_huggingface import HuggingFaceEmbeddings

embedding =HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text="dhaka is the capital of bangladesh"
documents=[
    "bangladesh is a small country ",
    "paris is the capital of france ",
    "london is the capital of england "
]

vector=embedding.embed_query(text) # Embedding a single query
vector1=embedding.embed_documents(documents) # Embedding multiple documents

print(str(vector))
print(str(vector1))