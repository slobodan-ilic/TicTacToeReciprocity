from ..model.db_manager import DatabaseManager as dbm
from board_controller import BoardController
from . import create_player
from ..model.enums.player_type import PlayerType
from ..model.enums.game_type import GameType
from ..model.enums.result import Result
from ..model.enums.player_role import PlayerRole


class GameController(object):
    def __init__(self, game_id=0):
        self.game = dbm.get_game_by_id(game_id).first()
        if self.game is not None:
            self._init_from_game()

    def create_new_game(self, m, n, k, game_type, user_x_id, user_o_id):
        self.game = dbm.create_new_game(m, n, k, game_type, user_x_id,
                                        user_o_id)
        self._init_from_game()

    def play(self, user_id, pos):
        if self.game.type == GameType.SingleUserHumanVsHuman:
            self.board_ctrl.play(pos)
        else:
            playing = self._who_is_trying_to_play(user_id)
            turn = self.board_ctrl.result()
            # print playing
            # print turn
            if (playing, turn) in [(PlayerRole.X, Result.PlayerXTurn),
                                   (PlayerRole.O, Result.PlayerOTurn)]:
                self.board_ctrl.play(pos)
                res = self.board_ctrl.result()
                if res == Result.PlayerXTurn:
                    self.player_x.notify()
                elif res == Result.PlayerOTurn:
                    self.player_o.notify()
        return self.board_ctrl.result()

    def get_user_game_info(self, user_id):
        if user_id == self.game.user_x_id:
            played_as = PlayerRole.X
        else:
            played_as = PlayerRole.O
        won_by = self.board_ctrl.result()
        return self.game.id, played_as, won_by

    def quit_game(self):
        dbm.delete_game_by_id(self.game.id)

    def _init_from_game(self):
        self.board_ctrl = BoardController(self.game.id)
        ai_player_types = [PlayerType.SimpleAI, PlayerType.PerfectAI]

        if self.game.user_x_id in ai_player_types:
            self.player_x = create_player(self.game.user_x_id,
                                          self.game.user_x_id, self)
            self.player_o = create_player(self.game.user_o_id,
                                          PlayerType.Human, self)
        elif self.game.user_o_id in ai_player_types:
            self.player_x = create_player(self.game.user_x_id,
                                          PlayerType.Human, self)
            self.player_o = create_player(self.game.user_o_id,
                                          self.game.user_o_id, self)
        elif self.game.type == GameType.SingleUserHumanVsHuman:
            self.player_x = create_player(self.game.user_x_id,
                                          PlayerType.Human, self)
            self.player_o = create_player(self.game.user_o_id,
                                          PlayerType.Human, self)

        self.board_ctrl = BoardController(self.game.board.first().id)

    def _who_is_trying_to_play(self, user_id):
        if user_id == self.player_x.user_id:
            return PlayerRole.X
        elif user_id == self.player_o.user_id:
            return PlayerRole.O
        else:
            raise Exception("Unknown user tried to play!")
