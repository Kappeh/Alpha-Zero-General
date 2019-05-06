from player import Player
from .tictactoe_game import Tictactoe_Game as Game

class Tictactoe_Solver:

    def __init__(self):
        self.game = Game()
    
    def predict(self, state_history, player):
        actions = state_history[-1].legal_actions()
        if state_history[-1].game_finished():
            return state_history[-1].winner * player, None
        multiplier = player * state_history[-1].player
        value, action = max((-self.negamax(self.game.next_state(state_history, a)), a) for a in actions)
        return value * multiplier, action
    
    def negamax(self, state):
        if state.game_finished():
            return state.winner * state.player
        actions = state.legal_actions()
        return max(-self.negamax(self.game.next_state([state], a)) for a in actions)