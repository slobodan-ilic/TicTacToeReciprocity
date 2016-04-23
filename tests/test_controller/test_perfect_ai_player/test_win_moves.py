from tests.test_controller.test_perfect_ai_player import TestPerfectAIPlayer


class TestWinMoves(TestPerfectAIPlayer):
    def test_win_move_complete_row_at_right_upper_corner_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("XX-"
                             "--O"
                             "OXO")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("XXX"
                                 "--O"
                                 "OXO")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_win_move_complete_row_at_right_upper_corner_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("OO-"
                             "X-X"
                             "XOX")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string = ("OOO"
                                 "X-X"
                                 "XOX")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_win_move_complete_row_at_left_upper_corner_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("-XX"
                             "--O"
                             "OXO")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("XXX"
                                 "--O"
                                 "OXO")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_win_move_complete_row_at_upper_middle_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("X-X"
                             "--O"
                             "OXO")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("XXX"
                                 "--O"
                                 "OXO")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_win_move_complete_col_at_right_upper_corner_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("X--"
                             "--O"
                             "XXO")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string = ("X-O"
                                 "--O"
                                 "XXO")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_win_move_complete_col_at_middle_left_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("OX-"
                             "-XX"
                             "O--")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string = ("OX-"
                                 "OXX"
                                 "O--")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_win_move_second_diagonal_at_right_upper_corner_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("---"
                             "OXO"
                             "X--")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("--X"
                                 "OXO"
                                 "X--")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_win_move_main_diagonal_at_middle_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("O--"
                             "X-X"
                             "X-O")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string = ("O--"
                                 "XOX"
                                 "X-O")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)
