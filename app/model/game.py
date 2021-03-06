from ..model import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), nullable=False)
    user_x_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                          nullable=False)
    user_o_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    board = db.relationship(
        'Board', backref='game', cascade='all, delete', lazy='dynamic')
