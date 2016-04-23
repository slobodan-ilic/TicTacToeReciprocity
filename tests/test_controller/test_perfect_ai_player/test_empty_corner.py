from tests.test_controller.test_perfect_ai_player import TestPerfectAIPlayer


class TestEmptyCorner(TestPerfectAIPlayer):
    def test_opposite_corner_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("---"
                             "-X-"
                             "---")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string_1 = ("---"
                                   "-X-"
                                   "--O")
        expected_board_string_2 = ("--O"
                                   "-X-"
                                   "---")
        expected_board_string_3 = ("O--"
                                   "-X-"
                                   "---")
        expected_board_string_4 = ("---"
                                   "-X-"
                                   "O--")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string in [expected_board_string_1,
                                                expected_board_string_2,
                                                expected_board_string_3,
                                                expected_board_string_4])

    def test_opposite_corner_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("O--"
                             "-X-"
                             "---")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string_1 = ("O-X"
                                   "-X-"
                                   "---")
        expected_board_string_2 = ("O--"
                                   "-X-"
                                   "--X")
        expected_board_string_3 = ("O--"
                                   "-X-"
                                   "X--")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string in [expected_board_string_1,
                                                expected_board_string_2,
                                                expected_board_string_3])
