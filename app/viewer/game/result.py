from . import game
from flask import render_template, redirect, request, session, url_for
from app.controller.game_controller import GameController
from flask.ext.login import login_required


@game.route('/result', methods=['GET', 'POST'])
@login_required
def result():
    game_id = session.get('GAME_ID', None)
    game_ctrl = GameController(game_id)
    if game_ctrl.game is None:
        return redirect(url_for('user.choose_game'))

    if request.method == 'POST':
        if 'btn_play_again' in request.form:
            session.pop('GAME_ID')
            return redirect(url_for('user.choose_game'))
    res = game_ctrl.board_ctrl.result()
    return render_template('game/result.html', res=res)
