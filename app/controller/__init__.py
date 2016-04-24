from ..model.enums.player_type import PlayerType
from .human_player import HumanPlayer
from .simple_ai_player import SimpleAIPlayer
from .perfect_ai_player import PerfectAIPlayer
from .network_player import NetworkPlayer


def create_player(user_id, player_type, game_controller):
    if player_type == PlayerType.Human:
        player = HumanPlayer(user_id, game_controller)
    elif player_type == PlayerType.SimpleAI:
        player = SimpleAIPlayer(user_id, game_controller)
    elif player_type == PlayerType.PerfectAI:
        player = PerfectAIPlayer(user_id, game_controller)
    elif player_type == PlayerType.Network:
        player = NetworkPlayer(user_id, game_controller)
    else:
        raise TypeError('Wrong player type.')
    return player
