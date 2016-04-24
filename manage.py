import os
from app import create_app, db
from app.model.board import Board
from app.model.user import User
from app.model.game import Game
from flask.ext.script import Manager, Shell


app, socketio = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Board=Board, User=User, Game=Game)
manager.add_command('shell', Shell(make_context=make_shell_context))


@manager.command
def run():
    socketio.run(app, debug=True)

if __name__ == '__main__':
    manager.run()
