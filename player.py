class Player:
    
    def __init__(self, game, name = 'Player'):
        self.game = game
        self.name = name

    def get_name(self):
        return self.name

    def get_action(self, state_history):
        pass