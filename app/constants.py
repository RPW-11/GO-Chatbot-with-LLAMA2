from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY=os.getenv('PINECONE_API_KEY')
PINECONE_ENV_NAME=os.getenv('PINECONE_ENV_NAME')
PINECONE_INDEX=os.getenv('PINECONE_INDEX')
EMBEDDINGS=os.getenv('EMBEDDINGS')

PROMP_TEMPLATE = """
Use the following informations to answer the question.
If the informations given are irrelevant, don't answer the question.

Context: {context}
Question: {question}

Only return helpful answers below and nothing else.
Answer:
"""
TEMPLATE_INPUT_VARIABLES = ['context', 'question']