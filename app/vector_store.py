from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from constants import PINECONE_API_KEY, PINECONE_INDEX, EMBEDDINGS


_pinecone_client = Pinecone(api_key=PINECONE_API_KEY)
_embedding = HuggingFaceEmbeddings(model_name=EMBEDDINGS)
pine_vectorstore = PineconeVectorStore(index=_pinecone_client.Index(PINECONE_INDEX), embedding=_embedding)
