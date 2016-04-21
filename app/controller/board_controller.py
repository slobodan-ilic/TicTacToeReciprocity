from ..model.enums.player import Player
from ..model.enums.result import Result
from ..model.db_manager import DatabaseManager as dbm


class BoardController(object):
    def __init__(self, board_id=0):
        self.board = dbm.get_board_by_id(board_id)

    def create_new_board(self, m, n, k):
        self.board = dbm.create_new_board(m, n, k)

    def play(self, pos):
        if self.result() in [Result.PlayerXTurn, Result.PlayerOTurn]:
            return self._make_move(pos)
        return self.result()

    def result(self):
        if not self._is_consistent():
            return Result.NonConsistent
        elif self._did_player_win(Player.X):
            return Result.WonByPlayerX
        elif self._did_player_win(Player.O):
            return Result.WonByPlayerO
        else:
            return self._get_player_turn()

    def display_board(self):
        board_symbols = [[self._symbol_at(i, j) for j in range(self.board.n)]
                         for i in range(self.board.m)]
        return board_symbols

    def get_moves(self):
        return self._extract_moves_from_string()

    def _make_move(self, pos):
        i = pos[0]
        j = pos[1]
        index = i * self.board.m + j
        x_moves, o_moves = self._extract_moves_from_string()

        if (self._get_player_turn() == Result.PlayerXTurn and
                index not in x_moves and index not in o_moves):
            self.board.x_moves += str(index) + ','
        elif (self._get_player_turn() == Result.PlayerOTurn and
                index not in o_moves and index not in x_moves):
            self.board.o_moves += str(index) + ','
        else:
            return Result.IrregularMove

        dbm.update_board_in_db(self.board)
        return self.result()

    def _did_player_win(self, player):
        """Check only for 3x3 board, to be extended for m,n,k game"""
        if self.board.m == 3 and self.board.n == 3:
            return (self._check_horizontal(player) or
                    self._check_vertical(player) or
                    self._check_main_diagonal(player) or
                    self._check_secondary_diagonal(player))
        else:
            raise NotImplementedError("Must be 3x3 game.")

    def _check_horizontal(self, player):
        b = self.display_board()
        return any([all(map(lambda x: x[2] == player, row)) for row in b])

    def _check_vertical(self, player):
        b = self.display_board()
        b_trans = [list(i) for i in zip(*b)]
        return any([all(map(lambda x: x[2] == player, row)) for row in b_trans])

    def _check_main_diagonal(self, player):
        m = self.board.m
        b = self.display_board()
        main_diagonal = [b[i][i] for i in range(m)]
        return all(map(lambda x: x[2] == player, main_diagonal))

    def _check_secondary_diagonal(self, player):
        m = self.board.m
        b = self.display_board()
        secondary_diag = [b[i][m - i - 1] for i in range(m)]
        return all(map(lambda x: x[2] == player, secondary_diag))

    def _is_consistent(self):
        x_moves, o_moves = self._extract_moves_from_string()
        total_moves = len(x_moves) + len(o_moves)
        return total_moves <= self.board.m * self.board.n

    def _extract_moves_from_string(self):
        x_moves = []
        o_moves = []
        if self.board.x_moves != '':
            x_moves = map(int, self.board.x_moves.strip(',').split(','))
        if self.board.o_moves != '':
            o_moves = map(int, self.board.o_moves.strip(',').split(','))
        return x_moves, o_moves

    def _get_player_turn(self):
        x_moves, o_moves = self._extract_moves_from_string()
        if len(x_moves) > len(o_moves):
            return Result.PlayerOTurn
        elif len(x_moves) == len(o_moves):
            return Result.PlayerXTurn
        else:
            raise ValueError("x moves: {0}, o moves: {1}".format(x_moves, o_moves))

    def _symbol_at(self, i, j):
        x_moves, o_moves = self._extract_moves_from_string()
        index = i * self.board.m + j
        if index in x_moves:
            return i, j, Player.X
        elif index in o_moves:
            return i, j, Player.O
        else:
            return i, j, '-'
