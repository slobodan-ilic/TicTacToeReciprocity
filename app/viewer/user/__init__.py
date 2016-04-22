from flask import Blueprint

user = Blueprint('user', __name__)

import welcome
import choose_game
import my_games
import ranking
