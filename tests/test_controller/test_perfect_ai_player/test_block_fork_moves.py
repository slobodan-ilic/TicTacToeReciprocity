from tests.test_controller.test_perfect_ai_player import TestPerfectAIPlayer


class TestBlockForkMoves(TestPerfectAIPlayer):
    def test_force_defence_when_opponent_has_double_fork_chance_as_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("--X"
                             "-O-"
                             "X--")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string_1 = ("--X"
                                   "-OO"
                                   "X--")
        expected_board_string_2 = ("--X"
                                   "OO-"
                                   "X--")
        expected_board_string_3 = ("-OX"
                                   "-O-"
                                   "X--")
        expected_board_string_4 = ("--X"
                                   "-O-"
                                   "XO-")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string in [expected_board_string_1,
                                                expected_board_string_2,
                                                expected_board_string_3,
                                                expected_board_string_4])

    def test_block_fork_upper_left_as_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("--X"
                             "XO-"
                             "---")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string = ("O-X"
                                 "XO-"
                                 "---")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_block_quadruple_fork_case_1_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("O--"
                             "-X-"
                             "--X")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string_1 = ("O-O"
                                   "-X-"
                                   "--X")
        expected_board_string_2 = ("O--"
                                   "-X-"
                                   "O-X")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string in [expected_board_string_1,
                                                expected_board_string_2])

    def test_block_quadruple_fork_case_2_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("X--"
                             "-X-"
                             "--O")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string_1 = ("X-O"
                                   "-X-"
                                   "--O")
        expected_board_string_2 = ("X--"
                                   "-X-"
                                   "O-O")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string in [expected_board_string_1,
                                                expected_board_string_2])
