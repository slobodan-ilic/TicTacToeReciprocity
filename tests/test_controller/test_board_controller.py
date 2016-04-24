from tests.test_basics import BasicTestCase
from app.controller.game_controller import GameController, GameType


class TestBoardController(BasicTestCase):
    empty_table_string = (
        "---"
        "---"
        "---"
    )

    def create_and_init_board_controller(self):
        gc = GameController()
        gc.create_new_game(3, 3, 3, GameType.SingleUserHumanVsHuman,
                           0, 0)
        return gc.board_ctrl

    def test_init_board_controller_from_symbols_all_xs(self):
        expected_table_string = (
            "XXX"
            "XXX"
            "XXX"
        )
        expected_positions = [
            [(0, 0, 'X'), (0, 1, 'X'), (0, 2, 'X')],
            [(1, 0, 'X'), (1, 1, 'X'), (1, 2, 'X')],
            [(2, 0, 'X'), (2, 1, 'X'), (2, 2, 'X')],
        ]
        bc = self.create_and_init_board_controller()
        bc.init_from_string(expected_table_string)
        positions = bc.display_board()
        self.assertTrue(positions == expected_positions)
        table_string = bc.display_board_as_string()
        self.assertTrue(table_string == expected_table_string)

    def test_init_board_controller_from_symbols_all_os(self):
        expected_table_string = (
            "OOO"
            "OOO"
            "OOO"
        )
        expected_positions = [
            [(0, 0, 'O'), (0, 1, 'O'), (0, 2, 'O')],
            [(1, 0, 'O'), (1, 1, 'O'), (1, 2, 'O')],
            [(2, 0, 'O'), (2, 1, 'O'), (2, 2, 'O')],
        ]
        bc = self.create_and_init_board_controller()
        bc.init_from_string(expected_table_string)
        positions = bc.display_board()
        self.assertTrue(positions == expected_positions)
        table_string = bc.display_board_as_string()
        self.assertTrue(table_string == expected_table_string)

    def test_init_board_controller_from_symbols_all_dashes(self):
        expected_table_string = (
            "---"
            "---"
            "---"
        )
        expected_positions = [
            [(0, 0, '-'), (0, 1, '-'), (0, 2, '-')],
            [(1, 0, '-'), (1, 1, '-'), (1, 2, '-')],
            [(2, 0, '-'), (2, 1, '-'), (2, 2, '-')],
        ]
        bc = self.create_and_init_board_controller()
        bc.init_from_string(expected_table_string)
        positions = bc.display_board()
        self.assertTrue(positions == expected_positions)
        table_string = bc.display_board_as_string()
        self.assertTrue(table_string == expected_table_string)

    def test_x_player_plays_opening_at_center(self):
        bc = self.create_and_init_board_controller()
        bc.init_from_string(self.empty_table_string)
        pos = (1, 1, 'X')
        bc.play(pos)
        expected_board_string = (
            "---"
            "-X-"
            "---"
        )
        result_board_string = bc.display_board_as_string()
        self.assertTrue(expected_board_string == result_board_string)

    def test_x_player_plays_opening_at_upper_right(self):
        bc = self.create_and_init_board_controller()
        bc.init_from_string(self.empty_table_string)
        pos = (0, 0, 'X')
        bc.play(pos)
        expected_board_string = (
            "X--"
            "---"
            "---"
        )
        result_board_string = bc.display_board_as_string()
        self.assertTrue(expected_board_string == result_board_string)

    def test_x_player_plays_opening_at_upper_middle(self):
        bc = self.create_and_init_board_controller()
        bc.init_from_string(self.empty_table_string)
        pos = (0, 1, 'X')
        bc.play(pos)
        expected_board_string = (
            "-X-"
            "---"
            "---"
        )
        result_board_string = bc.display_board_as_string()
        self.assertTrue(expected_board_string == result_board_string)
