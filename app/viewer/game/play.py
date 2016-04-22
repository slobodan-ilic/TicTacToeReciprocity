from . import game
from flask import render_template, redirect, request, session, url_for
from ...controller.game_controller import GameController, GameType, PlayerType
from ast import literal_eval as make_tuple
from app.model.enums.result import Result
from flask.ext.login import login_required


@game.route('/play', methods=['GET', 'POST'])
@login_required
def play():
    user_id = session.get('USER_ID', None)
    game_id = session.get('GAME_ID', None)
    game_ctrl = GameController(game_id)
    if game_ctrl.game is None:
        return redirect(url_for('user.choose_game'))

    if request.method == 'POST':
        if 'btn_play' in request.form:
            pos = make_tuple(request.form['btn_play'])
            if game_ctrl.play(user_id, pos) in [Result.WonByPlayerO,
                                                Result.WonByPlayerX,
                                                Result.Draw]:
                return redirect(url_for('game.result'))
        elif 'btn_quit' in request.form:
            session.pop('GAME_ID')
            # TODO: Clean up
            return redirect(url_for('user.welcome'))
        return redirect(url_for('game.play'))
    board = game_ctrl.board_ctrl.display_board()
    return render_template('game/play.html', board=board)


@game.route('/start_simple_game')
def start_simple_game():
    user_id = session.get('USER_ID', None)
    game_ctrl = GameController()
    game_ctrl.create_new_game(3, 3, 3, GameType.SingleUserHumanVsHuman, user_id,
                              user_id)
    game_id = game_ctrl.game.id
    session['GAME_ID'] = game_id
    return redirect(url_for('game.play'))


@game.route('/start_simple_ai_game')
def start_simple_ai_game():
    user_id = session.get('USER_ID', None)
    game_ctrl = GameController()
    game_ctrl.create_new_game(3, 3, 3, GameType.HumanVsSimpleAI, user_id,
                              PlayerType.SimpleAI)
    game_id = game_ctrl.game.id
    session['GAME_ID'] = game_id
    return redirect(url_for('game.play'))
