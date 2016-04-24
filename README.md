# Tic Tac Toe - Reciprocity
Test project for interview @ Reciprocity

This project implements a simple Tic-Tac-Toe game, as a Flask
application. The user needs to create an account and log in, in order
to play. Once logged, the user has the possibility to choose between
Practice, Simple, Hard and Network player modes.
* **Practice**: Single user plays both X and O moves.
* **Easy**: User plays an X move, and the computer immediately chooses
a random option from available positions, and plays an O move.
* **Hard**: User plays an X move, and the computer immediately chooses
best move, based on a lookup table strategy, and plays an O move.
* **Network player**: User needs to select the option 'Network Player'
and invite one of the users currently logged in. The invited user will
see a modal, and if he accepts the game, both are redirected to a
network game view.

## Setup
Run the server with `python manage.py shell` and create a database file
by executing `db.create_all()`.

## Usage
Run the server with `python manage.py run`, and access the UI.
at [localhost:5000](http://localhost:5000/).

### Note
The command to run server must be `run` and not `runserver`, as normally
used with Manager module. This is done because the server is run
as Flask-SocketIO application.
