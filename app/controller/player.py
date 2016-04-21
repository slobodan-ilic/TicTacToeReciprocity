class Player(object):
    def __init__(self, user_id, game_controller):
        self.user_id = user_id
        self.game_controller = game_controller

    def notify(self):
        pass

    def play(self, pos):
        self.game_controller.play(self.user_id, pos)
