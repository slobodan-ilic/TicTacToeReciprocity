from . import user
from flask import render_template, redirect, request, url_for
from flask.ext.login import login_required


@user.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():
    if request.method == 'POST':
        if 'btn_new_game' in request.form:
            return redirect(url_for('user.choose_game'))
        elif 'btn_my_games' in request.form:
            return redirect(url_for('user.my_games'))
        elif 'btn_ranking' in request.form:
            return redirect(url_for('user.ranking'))
    return render_template('user/welcome.html')
