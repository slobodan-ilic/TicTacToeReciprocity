from tests.test_controller.test_perfect_ai_player import TestPerfectAIPlayer


class TestOppositeCorner(TestPerfectAIPlayer):
    def test_opposite_corner_opening_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("O--"
                             "-X-"
                             "---")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("O--"
                                 "-X-"
                                 "--X")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)

    def test_opposite_corner_closing_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("OXO"
                             "-X-"
                             "XO-")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("OXO"
                                 "-X-"
                                 "XOX")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)
