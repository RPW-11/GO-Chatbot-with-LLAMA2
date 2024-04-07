from database import db
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float


class Document (db.Model):
    __tablename__ = 'documents'

    # Attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    size = Column(Float, nullable=False)
    created_at = Column(Date, nullable=False)


    def __init__(self, user_id, title, size, created_at):
        self.user_id = user_id
        self.title = title
        self.size = size
        self.created_at = created_at


    def insert_document(self):
        db.session.add(self)
        db.session.commit()
        return True
    

    def get_by_id(document_id:int):
        document = Document.query.get(document_id)
        return document
    

    def get_all():
        documents = Document.query.all()
        return documents
    

    def as_dict(self):
        return {
            'user_id': self.user_id,
            'title': self.title,
            'size': self.size,
            'created_at': self.created_at
        }


    def __repr__(self):
        return f"<Document {self.title}>"
    
