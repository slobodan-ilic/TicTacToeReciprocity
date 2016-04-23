from tests.test_controller.test_perfect_ai_player import TestPerfectAIPlayer


class TestBlockWinMoves(TestPerfectAIPlayer):
    def test_block_move_main_diagonal_at_middle_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("O-X"
                             "X-O"
                             "X--")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string = ("O-X"
                                 "XOO"
                                 "X--")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_block_main_diagonal_at_upper_left_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("--X"
                             "XO-"
                             "--O")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("X-X"
                                 "XO-"
                                 "--O")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_block_left_col_at_bottom_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("OX-"
                             "O--"
                             "--X")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("OX-"
                                 "O--"
                                 "X-X")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)
