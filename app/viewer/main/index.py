from . import main
from flask import render_template, redirect, request, url_for, session
from flask.ext.login import current_user
from ...controller.game_controller import GameController


@main.route('/', methods=['GET', 'POST'])
def index():
    # Redirect authenticated user to welcome screen.
    if current_user.is_authenticated:
        return redirect(url_for('user.welcome'))
    # Do the index page logic.
    if request.method == 'POST':
        if 'btn_login' in request.form:
            return redirect(url_for('main.login'))
        elif 'btn_sign_up' in request.form:
            return redirect(url_for('main.sign_up'))
    return render_template('main/index.html')
