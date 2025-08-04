from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

embeddings = OllamaEmbeddings(model="llama3.2:1b")


file_path = "C:/Users/gmlab/Desktop/RAG/bitcoin.pdf"
loader = PyPDFLoader(file_path)
# data = loader.load_and_split()
# print(data)

url=""
api_key=""

qdrant_client = QdrantClient(
    url="https://524dc75c-5293-4753-a044-8e25f0fc1130.us-west-2-0.aws.cloud.qdrant.io:6333",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.2FnU6Md1s5IdE3axavlG0ZzgcPLZT9o4sWdwbX4HvmA"
)

print(qdrant_client.get_collections())


qdrant = QdrantVectorStore.from_documents(
    loader.load_and_split(),
    OllamaEmbeddings(model="llama3.2:1b"),
    url="https://524dc75c-5293-4753-a044-8e25f0fc1130.us-west-2-0.aws.cloud.qdrant.io:6333",
    prefer_grpc=True,
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.2FnU6Md1s5IdE3axavlG0ZzgcPLZT9o4sWdwbX4HvmA",
    collection_name="bitcoin",
)