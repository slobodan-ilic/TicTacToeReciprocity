from . import game
from flask import render_template, redirect, request, session, url_for
from ...controller.game_controller import GameController, GameType, PlayerType
from ast import literal_eval as make_tuple
from app.model.enums.result import Result
from flask.ext.login import login_required
from app import socketio
from ...model.enums.socket_events import SocketEvents
from ...model.enums.socket_namespaces import SocketNamespaces


@game.route('/network_play', methods=['GET', 'POST'])
@login_required
def network_play():
    # TODO: Refactor this to only use 'game.play' viewer function.
    user_id = session.get('USER_ID')
    game_id = session.get('GAME_ID', None) or int(request.form['inp_game'])
    session['GAME_ID'] = game_id
    game_ctrl = GameController(game_id)
    if game_ctrl.game is None:
        # TODO: Add info about other user quitting the game.
        return redirect(url_for('user.welcome'))
    if request.method == 'POST':
        if 'btn_play' in request.form:
            pos = make_tuple(request.form['btn_play'])
            if game_ctrl.play(user_id, pos) in [Result.WonByPlayerO,
                                                Result.WonByPlayerX,
                                                Result.Draw]:
                return redirect(url_for('game.result'))
        elif 'btn_quit' in request.form:
            session.pop('GAME_ID')
            game_ctrl.quit_game()
            return redirect(url_for('user.welcome'))
        return redirect(url_for('game.network_play'))
    board = game_ctrl.board_ctrl.display_board()
    return render_template('game/play.html', board=board)


@game.route('/start_network_game', methods=['POST'])
def start_network_game():
    invitee_id = session.get('USER_ID', None)
    inviter_id = int(request.form['inp_inviter'])
    game_ctrl = GameController()
    game_ctrl.create_new_game(3, 3, 3, GameType.NetworkHumanVsHuman,
                              invitee_id, inviter_id)
    game_id = game_ctrl.game.id
    session['GAME_ID'] = game_id
    data = {
        'inviter_id': inviter_id,
        'game_id': game_id
    }
    print "starting"
    print "inviter: ", inviter_id
    print "invitee: ", invitee_id
    socketio.emit(SocketEvents.AcceptedNetworkGame, data,
                  namespace=SocketNamespaces.Reciprocity)
    return redirect(url_for('game.network_play'))
