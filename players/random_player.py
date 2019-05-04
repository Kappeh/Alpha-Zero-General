from random import choice
from player import Player

class Random_Player(Player):

    def __init__(self, game, name = 'Random Player'):
        super(Human_Player, self).__init__(game, name)
    
    def get_action(self, state_history):
        actions = self.game.legal_actions(state_history)
        return choice(actions)
