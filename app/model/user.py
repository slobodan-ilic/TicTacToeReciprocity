from ..model import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from app import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    score = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    currently_logged_in = db.Column(db.Boolean, default=False)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow())

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
