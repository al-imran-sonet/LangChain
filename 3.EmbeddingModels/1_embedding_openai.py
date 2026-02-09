from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

vector=embedding.embed_query("dhaka is the capital of bangladesh")

print(str(vector))