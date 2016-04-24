from tests.test_basics import BasicTestCase
import sqlalchemy
from app.model.game import Game
from app.model import db
from app.model.enums.game_type import GameType


class TestGame(BasicTestCase):
    def add_single_game_to_db(self):
        game = Game(user_x_id=0, user_o_id=1,
                    type=GameType.SingleUserHumanVsHuman)
        db.session.add(game)
        db.session.commit()
        return game.id

    def test_add_game_to_db(self):
        game_id = self.add_single_game_to_db()
        games = Game.query.all()
        self.assertTrue(len(games) == 1)
        game = Game.query.filter_by(id=game_id).first()
        self.assertTrue(game.id == game_id)

    def test_add_same_game_twice_integrity_error(self):
        game_id = self.add_single_game_to_db()
        game = Game(id=game_id, user_x_id=0, user_o_id=1,
                    type=GameType.SingleUserHumanVsHuman)
        db.session.add(game)
        self.assertRaises(sqlalchemy.exc.IntegrityError, db.session.commit)

    def test_add_game_without_type_integrity_error(self):
        game = Game(user_x_id=0, user_o_id=1)
        db.session.add(game)
        self.assertRaises(sqlalchemy.exc.IntegrityError, db.session.commit)

    def test_add_game_without_user_x_id_integrity_error(self):
        game = Game(user_o_id=0, type=GameType.SingleUserHumanVsHuman)
        db.session.add(game)
        self.assertRaises(sqlalchemy.exc.IntegrityError, db.session.commit)
