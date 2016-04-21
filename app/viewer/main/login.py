from . import main
from flask import render_template, redirect, url_for, flash, request, session
from app.viewer.forms.login_form import LoginForm
from flask.ext.login import login_user
from app.model.user import User


@main.route('/login', methods=['GET', 'POST'])
def login():
    frm_login = LoginForm()
    if frm_login.validate_on_submit():
        user = User.query.filter_by(username=frm_login.username.data).first()
        if user is not None and user.verify_password(frm_login.password.data):
            login_user(user)
            session['USER_ID'] = user.id
            return redirect(request.args.get('next') or
                            url_for('user.welcome'))
        flash("Invalid username or password.")
    return render_template('main/login.html', frm_login=frm_login)
