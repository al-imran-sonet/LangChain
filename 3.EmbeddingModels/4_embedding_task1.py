# we have some document and based on question we will find most relatable doucument 

from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity 
import numpy as np 
embedding= HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents=["True stability is found not in motion, but in standing parallel to the horizon.",
"Strength is a pillar that reaches for the sky without leaning into the wind.",
"They traveled toward the same horizon, always together but destined never to touch.",
"Every meeting of opposing forces creates a perfect corner for something new to begin.",
"The edge of a thing is where its story ends and the rest of the world starts.",
"What is unseen still holds a shape, even if the eye cannot trace its path.",
"A story is not a single thread, but a series of distinct moments connected by intent.",
"There is a rhythm in the rise and fall that mirrors the pulse of the sea.",
"Energy is rarely a straight path; it is the sharp, sudden turn that defines the spark.",
"We are defined not just by where we are, but by the phantom versions of where we might have been."
]

question= str(input("enter the question :"))

doc_embed=embedding.embed_documents(documents) # embedding multiple documents
question_embed=embedding.embed_query(question) # embedding single query


# calculate cosine similarity between question and documents

similarity =cosine_similarity([question_embed],doc_embed)[0]

# print(similarity.max())
# print(np.argmax(similarity))


# another way 

index,score=sorted(list(enumerate(similarity)),key=lambda x:x[1])[-1]
print(question)
print(documents[index])
print("similarity score : ",score)
