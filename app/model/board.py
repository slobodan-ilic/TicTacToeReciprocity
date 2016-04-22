import os
from ..model import db
from ..config import config

MAX_DB_STRING_SIZE = config[
    (os.getenv('FLASK_CONFIG') or 'default')].MAX_DB_STRING_SIZE


class Board(db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    m = db.Column(db.Integer)
    n = db.Column(db.Integer)
    k = db.Column(db.Integer)
    x_moves = db.Column(db.String(MAX_DB_STRING_SIZE))
    o_moves = db.Column(db.String(MAX_DB_STRING_SIZE))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    # game = db.relationship('Game',
    #                        backref=db.backref('Board',
    #                                           single_parent=True,
    #                                           cascade='all, delete'))
