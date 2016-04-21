from . import user
from flask import render_template, redirect, request, session, url_for
from app.controller.board_controller import BoardController
from ast import literal_eval as make_tuple
from app.model.enums.result import Result
from flask.ext.login import login_required


@user.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():
    if request.method == 'POST':
        if 'btn_new_game' in request.form:
            return redirect(url_for('user.choose_game'))
        elif 'btn_my_games' in request.form:
            return redirect(url_for('user.my_games'))
    return render_template('user/welcome.html')
