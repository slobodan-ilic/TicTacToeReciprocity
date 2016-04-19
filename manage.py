from app import create_app, db
from flask.ext.script import Manager, Shell

app = create_app('development')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)
manager.add_command('shell', Shell(make_context=make_shell_context))


@app.route('/')
def hello_world():
    return 'Tic Tac Toe - Reciprocity!'


if __name__ == '__main__':
    manager.run()
