from app import db
from werkzeug.security import generate_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, email, password):
        self.email =email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"<User: {self.email}>"

    def to_dict(self):
        return {'id': self.id, 'email': self.email, 'password': 'classified', 'created_on': self.created_on} #'id' NOT id...

    def from_dict(self, data): #New method to update user email and password; passes data into for loop and updates one at a time...
        for field in ['email', 'password']:
            if field in data:
                if field == 'password':
                    setattr(self, field, generate_password_hash(data[field]))
                else:
                    setattr(self, field, data[field])

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id


    def __repr__(self):
        return f"<Blog | {self.title}>"

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'content': self.content, 'user_id': self.user_id, 'created_on': self.created_on}

    def from_dict(self, data):  # New method to update blog; passes data into for loop and updates one at a time...
        for field in ['title', 'content', 'user_id']:
            setattr(self, field, data[field])