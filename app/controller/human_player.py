from .player import Player
from ..model.enums.player_type import PlayerType


class HumanPlayer(Player):
    def __init__(self, user_id, game_controller):
        Player.__init__(self, user_id, game_controller)
        self.player_type = PlayerType.Human
