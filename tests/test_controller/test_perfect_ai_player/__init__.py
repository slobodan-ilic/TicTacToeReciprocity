from tests.test_basics import BasicTestCase
from app.controller.game_controller import GameController, GameType
from app.model.enums.player_type import PlayerType


class TestPerfectAIPlayer(BasicTestCase):
    def create_game_controller_with_player_x_as_ai(self):
        gc = GameController()
        gc.create_new_game(
            3, 3, 3, GameType.HumanVsPerfectAI,
            user_x_id=PlayerType.PerfectAI, user_o_id=0)
        return gc

    def create_game_controller_with_player_o_as_ai(self):
        gc = GameController()
        gc.create_new_game(
            3, 3, 3, GameType.HumanVsPerfectAI,
            user_x_id=0, user_o_id=PlayerType.PerfectAI)
        return gc
