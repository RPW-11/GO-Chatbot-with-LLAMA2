from database import db
from sqlalchemy import Column, Integer, String, Date, CheckConstraint


class User (db.Model):
    __tablename__ = 'users'
    # Table attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(Date, nullable=False)
    role = Column(String, default='user')

    __table_args__ = (
        CheckConstraint(role.in_(['user', 'admin', 'llm']), name='role_types'),
    )


    def __init__(self, username, created_at, role=None):
        self.username = username
        self.created_at = created_at
        self.role = role


    def register_use_if_not_exists(self):
        user = User.query.filter(User.username == self.username).all()
        if not user:
            db.session.add(self)
            db.session.commit()

        return True
    

    def get_by_username(username):
        user = User.query.filter(User.username == username).first()

        return user
    

    def __repr__(self):
        return f"<User {self.username}>"