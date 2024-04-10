from llm import get_qaengine
from models.user import User
from models.document import Document
from datetime import date
from random import random


def register(username: str) -> bool:
    created_at = date.today()
    return User(username=username, created_at=created_at).register_use_if_not_exists()


def add_document(user_id:int, title:str, topic:str, tag:str):
    created_at = date.today()
    size = random() * 5
    return Document(user_id=user_id, title=title, topic=topic, tag=tag, size=size, created_at=created_at).insert_document()


def get_all_documents(page, per_page):
    documents = []
    for document in Document.get_all(page=page, per_page=per_page):
        documents.append(document.as_dict())
    return documents


def get_filtered_documents(filter_dict:dict):
    documents = []
    for document in Document.get_filtered_document(tags=filter_dict.get('tags'), search_term=filter_dict.get('search_term')):
        documents.append(document.as_dict())
    return documents


def delete_document_by_id(document_id:int)->bool:
    try:
        Document.delete_by_id(document_id=document_id)
        return True
    except:
        return False


def get_answer (question: str) -> str:
    qa_engine = get_qaengine()
    print("Inferencing....")
    print(f"Question: {question}")
    res = qa_engine.invoke(question)
    print("Done")
    print(res)
    return res