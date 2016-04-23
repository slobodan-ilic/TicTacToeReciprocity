from . import db
from game import Game
from board import Board
from user import User
from sqlalchemy import or_


class DatabaseManager(object):
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def get_user_by_name(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def update_user_logged_in(user_id):
        user = User.query.filter_by(id=user_id).first()
        user.currently_logged_in = True
        db.session.commit()

    @staticmethod
    def update_user_logged_out(user_id):
        user = User.query.filter_by(id=user_id).first()
        user.currently_logged_in = False
        db.session.commit()

    @staticmethod
    def get_all_user_ids():
        for user in User.query:
            yield user.id

    @staticmethod
    def get_game_by_id(game_id):
        return Game.query.filter_by(id=game_id)

    @staticmethod
    def get_board_by_id(board_id):
        return Board.query.filter_by(id=board_id).first()

    @staticmethod
    def create_new_board(m, n, k, game_id):
        board = Board(m=m, n=n, k=k, x_moves='', o_moves='', game_id=game_id)
        db.session.add(board)
        db.session.commit()
        return board

    @staticmethod
    def update_board(updated_board):
        board_id = updated_board.id
        board = Board.query.filter_by(id=board_id).first()
        board.x_moves = updated_board.x_moves
        board.o_moves = updated_board.o_moves
        db.session.commit()

    @staticmethod
    def create_new_game(m, n, k, game_type, user_x_id, user_o_id):
        game = Game(type=game_type, user_x_id=user_x_id, user_o_id=user_o_id)
        db.session.add(game)
        db.session.commit()
        DatabaseManager.create_new_board(m, n, k, game.id)
        return game

    @staticmethod
    def delete_game_by_id(game_id):
        game = Game.query.filter_by(id=game_id).first()
        db.session.delete(game)
        db.session.commit()

    @staticmethod
    def get_games_by_user_id(user_id):
        games = Game.query.filter(or_(Game.user_x_id==user_id,
                                      Game.user_o_id==user_id)).all()
        return games

    @staticmethod
    def get_currently_logged_users(user_id):
        users = User.query.filter_by(currently_logged_in=True)
        return [user.username for user in users if user.id != user_id]
