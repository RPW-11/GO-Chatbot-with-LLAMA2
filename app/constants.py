from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

PINECONE_API_KEY=os.getenv('PINECONE_API_KEY')
PINECONE_ENV_NAME=os.getenv('PINECONE_ENV_NAME')
PINECONE_INDEX=os.getenv('PINECONE_INDEX')
EMBEDDINGS=os.getenv('EMBEDDINGS')

PROMP_TEMPLATE = """
You are some who is very polite. You need to use the following informations to answer the question. Do not ever answer the question if it's irrelevant to the given informations.

Informations: {context}
Question: {question}

Make the answer clear and easy to understand.
Answer:
"""
TEMPLATE_INPUT_VARIABLES = ['context', 'question']