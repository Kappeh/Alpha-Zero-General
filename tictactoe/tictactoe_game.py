import numpy as np

from game import Game
from .tictactoe_state import Tictactoe_State

class Tictactoe_Game(Game):

    def __init__(self):
        pass
    
    def board_tensor_size(self):
        return [2, 3, 3]
    
    def status_tensor_size(self):
        return None
    
    def starting_state(self):
        return Tictactoe_State()
    
    def current_player(self, state_history):
        return state_history[-1].player

    def legal_actions(self, state_history, one_hot = False):
        return state_history[-1].legal_actions(one_hot = one_hot)

    def legal_action(self, state_history, action):
        return state_history[-1].legal_action(action)

    def next_state(self, state_history, action):
        result = state_history[-1].copy()
        return result.apply_action(action)
    
    def game_finished(self, state_history):
        return state_history[-1].game_finished()
    
    def winner(self, state_history):
        return state_history[-1].winner
    
    def board_tensor(self, state, player = None):
        return state.board_tensor(player)

    def status_tensor(self, state, player = None):
        return None

    def copy(self, state):
        return state.copy()
        
    def string(self, state):
        lines = []
        for i in range(0, 9, 3):
            line_strs = []
            for j in range(i, i + 3):
                if state.tiles[j] == Game.PLAYER_1:
                    line_strs.append('X')
                elif state.tiles[j] == Game.PLAYER_2:
                    line_strs.append('O')
                else:
                    line_strs.append('-')
            lines.append(''.join(line_strs))
        return '\n'.join(lines)

    def hash(self, state):
        return hash(state)