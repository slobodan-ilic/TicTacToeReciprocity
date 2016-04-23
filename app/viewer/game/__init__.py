from flask import Blueprint

game = Blueprint('game', __name__)

import play
import result
import network_play