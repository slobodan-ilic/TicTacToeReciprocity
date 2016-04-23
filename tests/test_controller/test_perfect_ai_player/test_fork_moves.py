from tests.test_controller.test_perfect_ai_player import TestPerfectAIPlayer


class TestForkMoves(TestPerfectAIPlayer):
    def test_fork_move_row_at_right_upper_corner_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("-X-"
                             "-OX"
                             "-O-")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("-XX"
                                 "-OX"
                                 "-O-")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_fork_move_at_lower_left_corner_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("-X-"
                             "OXX"
                             "-O-")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string = ("-X-"
                                 "OXX"
                                 "OO-")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_fork_move_at_middle_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("-X-"
                             "O-X"
                             "XOO")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("-XX"
                                 "O-X"
                                 "XOO")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)
