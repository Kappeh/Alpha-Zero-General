from player import Player
from mcts import MCTS

class NNet_Player(Player):

    def __init__(self, game, nnet, name = 'Neural Network Player'):
        super(NNet_Player, self).__init__(game, name)
        self.nnet = nnet
        self.mcts = MCTS(game, nnet, simulations = 800, c = 1.4)
    
    def get_action(self, state_history):
        return self.mcts.get_play(state_history)