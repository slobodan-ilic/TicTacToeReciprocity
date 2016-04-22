from . import user
from flask import render_template, session
from flask.ext.login import login_required
from ...controller.game_controller import GameController
from ...model.db_manager import DatabaseManager as dbm


@user.route('/my_games', methods=['GET', 'POST'])
@login_required
def my_games():
    user_id = session.get('USER_ID')
    games = dbm.get_games_by_user_id(user_id)
    user_games_info = []
    for game in games:
        ctrl = GameController(game.id)
        user_games_info.append(ctrl.get_user_game_info(user_id))

    return render_template('user/my_games.html',
                           user_games_info=user_games_info)
