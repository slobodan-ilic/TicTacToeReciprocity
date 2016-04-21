from . import main
from flask import render_template, redirect, request, url_for
from flask.ext.login import current_user


@main.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('user.welcome'))
    if request.method == 'POST':
        if 'btn_login' in request.form:
            return redirect(url_for('main.login'))
        elif 'btn_sign_up' in request.form:
            return redirect(url_for('main.sign_up'))
    return render_template('main/index.html')
