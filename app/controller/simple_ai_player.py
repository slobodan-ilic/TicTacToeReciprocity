from player import Player
from ..model.enums.player_type import PlayerType
from random import randint


class SimpleAIPlayer(Player):
    def __init__(self, user_id, game_controller):
        Player.__init__(self, PlayerType.SimpleAI, game_controller)
        self.player_type = PlayerType.SimpleAI

    def notify(self):
        pos = self._get_best_move()
        self.play(pos)

    def _get_best_move(self):
        m = self.game_controller.board_ctrl.board.m
        n = self.game_controller.board_ctrl.board.n
        positions = range(m * n)
        x_moves, o_moves = self.game_controller.board_ctrl.get_moves()
        available_moves = [x for x in positions if x not in [x_moves, o_moves]]
        index = available_moves[randint(0, len(available_moves) - 1)]
        i, j = index % m, index / m
        return i, j, '-'
