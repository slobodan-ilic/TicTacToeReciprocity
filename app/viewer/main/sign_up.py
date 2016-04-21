from . import main
from flask import render_template, redirect, url_for
from app.viewer.forms.add_user_form import AddUserForm
from app.model.user import User
from app.model import db


@main.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    frm_add_user = AddUserForm()
    if frm_add_user.validate_on_submit():
        user = User(username=frm_add_user.username.data,
                    password=frm_add_user.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect((url_for('main.index')))
    return render_template('main/sign_up.html', frm_add_user=frm_add_user)
