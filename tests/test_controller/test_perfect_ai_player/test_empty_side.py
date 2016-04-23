from tests.test_controller.test_perfect_ai_player import TestPerfectAIPlayer


class TestEmptySide(TestPerfectAIPlayer):
    def test_empty_side_as_player_x(self):
        gc = self.create_game_controller_with_player_x_as_ai()
        init_board_string = ("XOX"
                             "-OO"
                             "OXX")
        gc.board_ctrl.init_from_string(init_board_string)
        gc.player_x.notify()
        expected_board_string = ("XOX"
                                 "XOO"
                                 "OXX")
        result_board_string = gc.board_ctrl.display_board_as_string()
        self.assertTrue(result_board_string == expected_board_string)
