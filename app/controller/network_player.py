from .player import Player
from ..model.enums.player_type import PlayerType
from app import socketio
from ..model.enums.socket_events import SocketEvents
from ..model.enums.socket_namespaces import SocketNamespaces


class NetworkPlayer(Player):
    def __init__(self, user_id, game_controller):
        Player.__init__(self, user_id, game_controller)
        self.player_type = PlayerType.Human

    def notify(self):
        data = {
            'user_id': self.user_id,
            'updated_board': self.game_controller.board_ctrl.display_board(),
            'result': self.game_controller.board_ctrl.result()
        }
        socketio.emit(SocketEvents.PlayersTurn, data,
                      namespace=SocketNamespaces.Reciprocity)
