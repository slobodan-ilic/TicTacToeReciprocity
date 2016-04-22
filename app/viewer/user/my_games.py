from . import user
from flask import render_template, session
from flask.ext.login import login_required
from ...model.db_manager import DatabaseManager as dbm


@user.route('/my_games', methods=['GET', 'POST'])
@login_required
def my_games():
    user_id = session.get('USER_ID')
    games = dbm.get
    return render_template('user/welcome.html')
