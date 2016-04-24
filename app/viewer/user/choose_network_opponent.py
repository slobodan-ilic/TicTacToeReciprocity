from ..user import user
from flask import render_template, redirect, request, session, url_for
from app.model.db_manager import DatabaseManager as dbm
from flask.ext.login import login_required
from app import socketio
from flask.ext.socketio import emit
from ...model.enums.socket_events import SocketEvents
from ...model.enums.socket_namespaces import SocketNamespaces


@user.route('/choose_network_opponent', methods=['GET', 'POST'])
@login_required
def choose_network_opponent():
    user_id = session.get('USER_ID', None)
    names = dbm.get_currently_logged_users(user_id)
    return render_template(
        'user/choose_network_opponent.html', names=names)


@socketio.on(SocketEvents.InviteNetworkPlayer,
             namespace=SocketNamespaces.Reciprocity)
@login_required
def invite_player(msg):
    current_user_id = session.get('USER_ID')
    invited_user = dbm.get_user_by_name(msg['invitedUserName'])
    invited_user_id = invited_user.id
    data = {
        'invitee_id': invited_user_id,
        'inviter_id': current_user_id
    }
    print "choose partner"
    print "inviter: ", current_user_id
    print "invitee: ", invited_user_id
    socketio.emit(SocketEvents.InviteNetworkPlayer, data,
                  namespace=SocketNamespaces.Reciprocity)
