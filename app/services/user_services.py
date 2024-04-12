from llm import get_qaengine
from models.user import User
from models.document import Document
from datetime import date
from random import random
from helpers.document import allowed_file
from werkzeug.utils import secure_filename
from uuid import uuid4
from constants import UPLOAD_FOLDER
import os



def register(username: str) -> bool:
    created_at = date.today()
    return User(username=username, created_at=created_at).register_use_if_not_exists()


def add_document(user_id:int, title:str, topic:str, files:dict):
    # check file
    if 'file' not in files:
        raise Exception("No file part")
    
    document_file = files.get('file')

    if document_file.filename == '':
        raise Exception("No selected file")
    
    if document_file and allowed_file(document_file.filename):
        id = uuid4()
        filename = secure_filename(document_file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, str(id) + '-' + filename )
        document_file.save(filepath)

        # store the document information in the database
        created_at = date.today()
        size = os.stat(filepath).st_size / (1000 * 1000) # in MB
        tag = document_file.filename.rsplit('.', 1)[1]

        return Document(id=id, user_id=user_id, title=title, original_name=filename, path=filepath, topic=topic, tag=tag, size=size, created_at=created_at).insert_document()
    
    else:
        raise Exception("File is not allowed")


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


def delete_document_by_id(document_id:str)->bool:
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