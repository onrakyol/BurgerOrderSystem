from datetime import datetime
from app import db, bcrypt

# Alias common DB names
Column = db.Column
Model = db.Model

class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class User(Model):    
    id = Column(db.Integer, primary_key=True)
    email = Column(db.String(64), unique=True, index=True)
    username = Column(db.String(15), unique=True, index=True)
    name = Column(db.String(64))
    password_hash = Column(db.String(128))
    joined_date = Column(db.DateTime, default=datetime.utcnow)
    roleId = Column(db.Integer) # 1 = Restoran, 2 = Müşteri


    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"