from enum import unique
from flask_sqlalchemy import SQLAlchemy
import uuid
import secrets
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow

login_manager = LoginManager()
ma = Marshmallow()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True, unique = True)
    email = db.Column(db.String(150), unique= True, nullable=False)
    password = db.Column(db.String, nullable = False)
    token = db.Column(db.String, nullable = False, unique=True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    favorite = db.relationship('Favorite', backref = 'owner', lazy = True)
    
    def __init__(self, email, password, token = '', id = ''):
        self.id = self.set_id()
        self.email = email
        self.password = self.set_password(password)
        self.token = self.get_token(24)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def get_token(self,length):
        return secrets.token_hex(length)

class Favorite(db.Model):
    id = db.Column(db.String, primary_key = True, unique = True)
    team = db.Column(db.String(100), nullable=False)
    player = db.Column(db.String(100), nullable = True)
    match = db.Column(db.String, nullable = True)
    explanation = db.Column(db.String, nullable = True)
    comments = db.Column(db.String, nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, team, player, match, explanation, comments, user_token, id = ''):
        self.id = self.set_id()
        self.team = team
        self.player = player
        self.match = match
        self.explanation = explanation
        self.comments = comments
        self.user_token = user_token

    def set_id(self):
        return str(uuid.uuid4())

class FavoriteSchema(ma.Schema):
    class Meta:
        fields = ['id', 'team', 'player', 'match', 'explanation', 'comments']

# create singular data point return
favorite_schema = FavoriteSchema()

# create multiple data point return
favorites_schema = FavoriteSchema(many = True)


