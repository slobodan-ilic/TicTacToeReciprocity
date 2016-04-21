from . import main
from flask import redirect, url_for, flash, session
from flask.ext.login import login_required, logout_user


@main.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('USER_ID')
    flash("You have been logged out.")
    return redirect(url_for('main.index'))
