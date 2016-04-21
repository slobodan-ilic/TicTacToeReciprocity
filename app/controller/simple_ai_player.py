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
        m = self.game_controller.board.m
        n = self.game_controller.board.n
        positions = range(m * n)
        x_moves, o_moves = self.game_controller.board.get_moves()
        available_moves = map(lambda x: x not in [x_moves, o_moves], positions)
        pos = available_moves[randint(len(available_moves) - 1)]
        return pos
