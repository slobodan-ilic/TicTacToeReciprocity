from . import user
from flask import render_template, redirect, request, session, url_for
from app.controller.board_controller import BoardController
from ast import literal_eval as make_tuple
from app.model.enums.result import Result
from flask.ext.login import login_required


@user.route('/choose_game', methods=['GET', 'POST'])
@login_required
def choose_game():
    if request.method == 'POST':
        if 'btn_practice' in request.form:
            return redirect(url_for('game.start_simple_game'))
        elif 'btn_simple_ai' in request.form:
            return redirect(url_for('game.start_simple_ai_game'))
        elif 'btn_perfect_ai' in request.form:
            return redirect(url_for('game.start_perfect_ai_game'))
        elif 'btn_network' in request.form:
            return redirect(url_for('user.choose_network_opponent'))
    return render_template('user/choose_game.html')
