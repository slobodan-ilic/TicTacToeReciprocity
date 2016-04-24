from tests.test_basics import BasicTestCase
from app.model.user import User
from uuid import uuid4


class TestMain(BasicTestCase):
    def add_user(self):
        username = str(uuid4())
        password = str(uuid4())
        confirm = password
        self.cli.post('/sign_up', data={
            'username': username,
            'password': password,
            'confirm': confirm
        }, follow_redirects=True)
        return username, password

    def test_index_view(self):
        res = self.cli.get('/')
        content = "Tic Tac Toe - Reciprocity"
        self.assertIn(content, res.data)

    def test_add_user_successfully(self):
        username, password = self.add_user()
        user = User.query.filter_by(username=username).first()
        self.assertEqual(user.username, username)

    def test_login_successfully(self):
        username, password = self.add_user()
        res = self.cli.post('/login', data={
            'username': username,
            'password': password
        }, follow_redirects=True)
        content = 'Welcome, ' + username
        self.assertIn(content, res.data)
