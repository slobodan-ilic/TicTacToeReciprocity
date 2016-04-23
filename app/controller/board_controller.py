from ..model.enums.player_role import PlayerRole
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
        elif self._did_player_win(PlayerRole.X):
            return Result.WonByPlayerX
        elif self._did_player_win(PlayerRole.O):
            return Result.WonByPlayerO
        elif self._is_draw():
            return Result.Draw
        else:
            return self._get_player_turn()

    def display_board(self):
        board_symbols = [[self._symbol_at(i, j) for j in range(self.board.n)]
                         for i in range(self.board.m)]
        return board_symbols

    def display_board_as_string(self):
        positions = self.display_board()
        board_string = [[pos[2] for pos in row] for row in positions]
        return ''.join(sum(board_string, []))

    def init_from_string(self, string):
        m = self.board.m
        n = self.board.n
        positions = [(i, j, string[i * m + j])
                     for i in range(m)
                     for j in range(n)]
        self.init_from_positions(positions)

    def init_from_positions(self, positions):
        x_moves = ''
        o_moves = ''
        m = self.board.m
        for pos in positions:
            i = pos[0]
            j = pos[1]
            index = i * m + j
            player = pos[2]
            if player == PlayerRole.X:
                x_moves += str(index) + ','
            elif player == PlayerRole.O:
                o_moves += str(index) + ','
            elif player == '-':
                continue
            else:
                raise ValueError('Wrong player symbol.')
        else:
            self.board.x_moves = x_moves
            self.board.o_moves = o_moves

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

        dbm.update_board(self.board)
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

    def _is_draw(self):
        if self.board.m == 3 and self.board.n == 3:
            n_max_allowed_moves = self.board.m * self.board.n
            x_moves, o_moves = self._extract_moves_from_string()
            n_played_moves = len(x_moves) + len(o_moves)
            return (n_played_moves == n_max_allowed_moves and
                    not self._did_player_win(PlayerRole.X) and
                    not self._did_player_win(PlayerRole.O))
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
            return i, j, PlayerRole.X
        elif index in o_moves:
            return i, j, PlayerRole.O
        else:
            return i, j, '-'
