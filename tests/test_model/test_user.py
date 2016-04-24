from uuid import uuid4
from app import db
from app.model.user import User
from tests.test_basics import BasicTestCase
import sqlalchemy


class TestUser(BasicTestCase):
    def add_single_user_to_db(self):
        username = str(uuid4())
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return username

    def test_add_single_user_to_db(self):
        username = self.add_single_user_to_db()
        users = User.query.all()
        self.assertTrue(len(users) == 1)
        user = User.query.first()
        self.assertTrue(user.username == username)

    def test_add_same_user_twice(self):
        username = self.add_single_user_to_db()
        user = User(username=username)
        db.session.add(user)
        self.assertRaises(sqlalchemy.exc.IntegrityError, db.session.commit)

    def test_remove_user(self):
        username = self.add_single_user_to_db()
        users = User.query.all()
        self.assertTrue(len(users) == 1)
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        users = User.query.all()
        self.assertTrue(len(users) == 0)
