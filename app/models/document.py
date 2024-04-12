from database import db
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, and_, or_, Uuid
from typing import List


class Document (db.Model):
    __tablename__ = 'documents'

    # Attributes
    id = Column(Uuid, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    original_name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    tag = Column(String, nullable=False)
    size = Column(Float, nullable=False)
    created_at = Column(Date, nullable=False)


    def __init__(self, id, user_id, title, original_name, path, topic, tag, size, created_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.original_name = original_name
        self.path = path
        self.topic = topic
        self.tag = tag
        self.size = size
        self.created_at = created_at


    def insert_document(self) -> bool:
        db.session.add(self)
        db.session.commit()
        return True
    

    def get_by_id(document_id:int):
        document = Document.query.get(document_id)
        return document
    

    def delete_by_id(document_id:int):
        Document.query.filter_by(id=document_id).delete()
        db.session.commit()
    

    def get_all(page:int, per_page:str):
        documents = Document.query.limit(per_page).offset(page*per_page).all()
        return documents
    

    def get_filtered_document(tags:list, search_term:str) -> List['Document']:
        documents = Document.query.filter(and_(
            Document.tag.in_(tags),
            or_(Document.topic.ilike(f"%{search_term}%"), Document.title.ilike(f"%{search_term}%"))
        )).all()
        return documents
    

    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'topic': self.topic,
            'tag': self.tag,
            'size': "{:.2f}".format(self.size),
            'created_at': self.created_at
        }


    def __repr__(self):
        return f"<Document {self.title}>"
    
