from . import db
from game import Game
from board import Board
from user import User


class DatabaseManager(object):
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def get_user_by_name(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_game_by_id(game_id):
        return Game.query.filter_by(id=game_id)

    @staticmethod
    def get_board_by_id(board_id):
        return Board.query.filter_by(id=board_id).first()

    # @staticmethod
    # def create_new_board(m, n, k):
    #     board = Board(m=m, n=n, k=k, x_moves='', o_moves='')
    #     db.session.add(board)
    #     db.session.commit()
    #     return board

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
    def create_new_game(m, n, k, game_type, user_x_id, user_o_id=None):
        game = Game(type=game_type, user_x_id=user_x_id, user_o_id=user_o_id)
        db.session.add(game)
        db.session.commit()
        print "game: ", game
        board = DatabaseManager.create_new_board(m, n, k, game.id)
        # game = Game(type=game_type, user_x_id=user_x_id, user_o_id=user_o_id,
        #             board_id=board.id)
        return game

    @staticmethod
    def delete_game_by_id(game_id):
        game = Game.query.filter_by(id=game_id).first()
        db.session.delete(game)
        db.session.commit()
