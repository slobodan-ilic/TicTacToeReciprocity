from . import user
from flask import render_template, session
from flask.ext.login import login_required
from ...controller.game_controller import GameController, PlayerRole, Result
from ...model.db_manager import DatabaseManager as dbm


@user.route('/ranking', methods=['GET', 'POST'])
@login_required
def ranking():
    users_scores = get_users_scores()
    return render_template('user/ranking.html', users_scores=users_scores)


def get_users_scores():
    users_ids = dbm.get_all_user_ids()
    users_scores = []
    for user_id in users_ids:
        users_scores.append((dbm.get_user_by_id(user_id).username,
                            get_user_score(user_id)))
    return users_scores


def get_user_score(user_id):
    games = dbm.get_games_by_user_id(user_id)
    score = 0
    for game in games:
        gc = GameController(game.id)
        game_info = gc.get_user_game_info(user_id)
        if game_info[1:] in [(PlayerRole.X, Result.WonByPlayerX),
                             (PlayerRole.O, Result.WonByPlayerO)]:
            score += 1
    return score
