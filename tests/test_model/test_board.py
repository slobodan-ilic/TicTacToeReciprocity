from uuid import uuid4
from app import db
import sqlalchemy
from app.model.board import Board
from tests.test_basics import BasicTestCase


class TestBoard(BasicTestCase):
    def add_single_board_to_db(self):
        board = Board(game_id=0)
        db.session.add(board)
        db.session.commit()
        return board.id

    def test_add_single_board_to_db(self):
        board_id = self.add_single_board_to_db()
        boards = Board.query.all()
        self.assertTrue(len(boards) == 1)
        board = Board.query.filter_by(id=board_id).first()
        self.assertTrue(board.id == board_id)

    def test_add_same_board_twice_integrity_error(self):
        board_id = self.add_single_board_to_db()
        board = Board(id=board_id)
        db.session.add(board)
        self.assertRaises(sqlalchemy.exc.IntegrityError, db.session.commit)

    def test_add_board_without_game_integrity_error(self):
        board = Board()
        db.session.add(board)
        self.assertRaises(sqlalchemy.exc.IntegrityError, db.session.commit)

    def test_remove_board_from_db(self):
        board_id = self.add_single_board_to_db()
        board = Board.query.filter_by(id=board_id).first()
        self.assertTrue(board.id == board_id)
        db.session.delete(board)
        boards = Board.query.all()
        self.assertTrue(len(boards) == 0)
