from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY=os.getenv('PINECONE_API_KEY')
PINECONE_ENV_NAME=os.getenv('PINECONE_ENV_NAME')
PINECONE_INDEX=os.getenv('PINECONE_INDEX')
EMBEDDINGS=os.getenv('EMBEDDINGS')

PROMP_TEMPLATE = """
As a customer support agent, your role is to provide factual information and assistance in a helpful manner. Maintain a friendly tone without being overly chatty. Respond to the query based on the provided context information only. If question can't be answered with the given context tell the question is irrelevant. Also, mention the given context.

Context: {context}
Question: {question}

Only return helpful answers below and nothing else.
Answer:
"""
TEMPLATE_INPUT_VARIABLES = ['context', 'question']