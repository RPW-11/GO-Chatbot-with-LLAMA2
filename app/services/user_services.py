from llm import get_qaengine
from models.user import User
from models.document import Document
from datetime import date
from random import random


def register(username: str) -> bool:
    created_at = date.today()
    return User(username=username, created_at=created_at).register_use_if_not_exists()


def add_document(user_id:int, title:str):
    created_at = date.today()
    size = random() * 5
    return Document(user_id=user_id, title=title, size=size, created_at=created_at).insert_document()


def get_all_documents():
    documents = []
    for document in Document.get_all():
        documents.append(document.as_dict())
    return documents


def get_answer (question: str) -> str:
    qa_engine = get_qaengine()
    print("Inferencing....")
    print(f"Question: {question}")
    res = qa_engine.invoke(question)
    print("Done")
    print(res)
    return res