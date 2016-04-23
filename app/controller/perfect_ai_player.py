from player import Player
from ..model.enums.player_type import PlayerType
from ..model.enums.complete_row import CompleteRow
from ..model.enums.player_role import PlayerRole


class PerfectAIPlayer(Player):
    def __init__(self, user_id, game_controller):
        Player.__init__(self, user_id, game_controller)
        self.player_type = PlayerType.PerfectAI

    def notify(self):
        pos = self._get_best_move()
        # print "pos: ", pos
        self.play(pos)

    def _get_best_move(self):
        user_game_info = self.game_controller.get_user_game_info(
            PlayerType.PerfectAI)
        playing_as = user_game_info[1]
        pos_win_or_block = self._win_or_block_move(playing_as)
        pos_fork = self._fork(playing_as)
        pos_block_fork = self._block_fork(playing_as)
        pos_center = self._mark_center(playing_as)
        pos_opposite_corner = self._play_opposite_corner(playing_as)
        pos_empty_corner = self._play_empty_corner()
        return (pos_win_or_block or pos_fork or pos_block_fork or pos_center or
                pos_opposite_corner or pos_empty_corner)

    def _play_empty_side(self):
        board = self.game_controller.board_ctrl.display_board()
        m = self.game_controller.board_ctrl.board.m
        n = self.game_controller.board_ctrl.board.n
        for i in range(m):
            for j in range(n):
                if i != j and i != m - i - 1:
                    print "pos: ", board[i][j]
                    symbol = board[i][j][2]
                    if symbol == '-':
                        return board[i][j]
        return None

    def _play_empty_corner(self):
        board = self.game_controller.board_ctrl.display_board()
        m = self.game_controller.board_ctrl.board.m
        n = self.game_controller.board_ctrl.board.n
        for i in [0, m - 1]:
            for j in [0, n - 1]:
                symbol = board[i][j][2]
                if symbol == '-':
                    return board[i][j]
        return None

    def _play_opposite_corner(self, playing_as):
        board = self.game_controller.board_ctrl.display_board()
        m = self.game_controller.board_ctrl.board.m
        n = self.game_controller.board_ctrl.board.n
        opponent_playing_as = self._opponent_playing_as(playing_as)
        for i in [0, m - 1]:
            for j in [0, n - 1]:
                corner = board[i][j]
                opposite_corner = board[m - i -1][n - j - 1]
                if (opposite_corner[2] == opponent_playing_as and
                        corner[2] == '-'):
                    return corner
        return None

    def _mark_center(self, playing_as):
        board = self.game_controller.board_ctrl.display_board()
        center_symbol = board[1][1][2]
        if center_symbol == '-':
            return board[1][1]
        return None

    def _block_fork(self, playing_as):
        opponent_playing_as = self._opponent_playing_as(playing_as)
        opponent_fork_positions = self._fork_positions(opponent_playing_as)
        if len(opponent_fork_positions) == 1:
            return opponent_fork_positions[0]
        elif len(opponent_fork_positions) > 1:
            return self._force_two_in_a_row(playing_as, opponent_fork_positions)
        return None

    def _force_two_in_a_row(self, playing_as, opponent_fork_positions):
        board, transposed_board, main_diagonal, second_diagonal =\
            self._get_board_important_lines()
        for row in (board + transposed_board + [main_diagonal] +
                        [second_diagonal]):
            pos = self.force_row(row, playing_as, opponent_fork_positions)
            if pos is not None:
                return pos
        return None

    def force_row(self, row, playing_as, opponent_fork_positions):
        pos = None
        counter = 0
        for e in row:
            symbol = e[2]
            if symbol == '-' and e not in opponent_fork_positions:
                pos = e
            elif symbol == playing_as:
                counter += 1
            else:
                return None
        else:
            if counter > 0:
                return pos
        return None

    def _opponent_playing_as(self, playing_as):
        if playing_as == PlayerRole.X:
            return PlayerRole.O
        elif playing_as == PlayerRole.O:
            return PlayerRole.X
        else:
            raise ValueError('Unknown player type.')

    def _fork(self, playing_as):
        fork_positions = self._fork_positions(playing_as)
        if len(fork_positions) > 0:
            return fork_positions[0]
        return None

    def _get_board_important_lines(self):
        board = self.game_controller.board_ctrl.display_board()
        m = self.game_controller.board_ctrl.board.m
        transposed_board = [list(i) for i in zip(*board)]
        main_diagonal = [board[i][i] for i in range(m)]
        secondary_diagonal = [board[i][m - i - 1] for i in range(m)]
        return board, transposed_board, main_diagonal, secondary_diagonal

    def _fork_positions(self, playing_as):
        board = self.game_controller.board_ctrl.display_board()
        m = self.game_controller.board_ctrl.board.m
        transposed_board = [list(i) for i in zip(*board)]
        main_diagonal = [board[i][i] for i in range(m)]
        secondary_diagonal = [board[i][m - i - 1] for i in range(m)]
        row_fork_positions = []
        common = []
        for row in board:
            row_fork_positions += self._row_fork_positions(row, playing_as)
        col_fork_positions = []
        for col in transposed_board:
            col_fork_positions += self._row_fork_positions(col, playing_as)
        common += list(set(row_fork_positions).intersection(
            set(col_fork_positions)))
        # if len(common) != 0:
        #     return common[0]
        # else:
        #     row_fork_positions += col_fork_positions
        row_fork_positions = list(set(
            row_fork_positions).union(set(col_fork_positions)))
        main_dg_fork_positions = []
        for d in [main_diagonal]:
            main_dg_fork_positions += self._row_fork_positions(d, playing_as)
        common += list(set(row_fork_positions).intersection(
            set(main_dg_fork_positions)))
        # if len(common) != 0:
        #     return common[0]
        # else:
        #     row_fork_positions += main_dg_fork_positions
        row_fork_positions = list(set(
            row_fork_positions).union(set(col_fork_positions)))
        sec_dg_fork_positions = []
        for d in [secondary_diagonal]:
            sec_dg_fork_positions += self._row_fork_positions(d, playing_as)
        common += list(set(row_fork_positions).intersection(
            set(sec_dg_fork_positions)))
        return common
        # if len(common) != 0:
        #     return common[0]
        # else:
        #     return None

    def _win_or_block_move(self, playing_as):
        board = self.game_controller.board_ctrl.display_board()
        transposed_board = [list(i) for i in zip(*board)]
        m = self.game_controller.board_ctrl.board.m
        main_diagonal = [board[i][i] for i in range(m)]
        secondary_diagonal = [board[i][m - i - 1] for i in range(m)]

        pos_win = None
        pos_block = None

        for row in (board + transposed_board + [main_diagonal] +
                    [secondary_diagonal]):
            pos_win = pos_win or self._complete_or_block_row(
                row, playing_as, CompleteRow.Win)
            pos_block = pos_block or self._complete_or_block_row(
                row, playing_as, CompleteRow.Block)
        return pos_win or pos_block

    def _complete_or_block_row(self, row, playing_as, complete_row):
        count = 0
        pos = None
        for e in row:
            symbol = e[2]
            if symbol == '-':
                pos = e
            elif complete_row == CompleteRow.Win:
                if symbol == playing_as:
                    count += 1
            elif complete_row == CompleteRow.Block:
                if symbol != playing_as:
                    count += 1
            else:
                return None
        else:
            if count >= 2:
                return pos
        return None

    def _row_fork_positions(self, row, playing_as):
        positions = []
        counter = 0
        for e in row:
            symbol = e[2]
            if symbol == '-':
                positions.append(e)
            elif symbol != playing_as:
                return []
            elif symbol:
                counter += 1
            else:
                raise ValueError('Unknown symbol.')
        else:
            if counter == 1:
                return positions
        return []
