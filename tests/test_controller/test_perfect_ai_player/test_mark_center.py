from tests.test_controller.test_perfect_ai_player import TestPerfectAIPlayer


class TestMarkCenter(TestPerfectAIPlayer):
    def test_mark_center_on_a_clean_board_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("---"
                             "---"
                             "---")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("---"
                                 "-X-"
                                 "---")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_mark_center_of_corner_opening_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("--X"
                             "---"
                             "---")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string = ("--X"
                                 "-O-"
                                 "---")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_mark_center_of_edbe_opening_as_player_o(self):
        gc = self.create_game_controller_with_player_o_as_ai()
        init_board_string = ("-X-"
                             "---"
                             "---")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_o.notify()
        expected_board_string = ("-X-"
                                 "-O-"
                                 "---")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)
