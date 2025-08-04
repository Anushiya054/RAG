from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from llm import completion_prompt


embeddings = OllamaEmbeddings(model="llama3.2:1b")

url = "https://524dc75c-5293-4753-a044-8e25f0fc1130.us-west-2-0.aws.cloud.qdrant.io:6333"
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.2FnU6Md1s5IdE3axavlG0ZzgcPLZT9o4sWdwbX4HvmA"

question = input("Enter your question: ")
    
   
qdrant = QdrantVectorStore.from_existing_collection(
     embedding=embeddings,
     collection_name="bitcoin",
     url=url,
     api_key=api_key,
)
    
    
response = qdrant.similarity_search(
    question, k=2  
)
prompt = f"""
Question: {question}

Context: {response}

You are a helpful assistant that can answer questions about the context provided.
"""

print("Prompt:", prompt)
print( completion_prompt(prompt))



    