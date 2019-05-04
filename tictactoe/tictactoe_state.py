import numpy as np

from game import Game
from zobrist import Hash

class Tictactoe_State:

    LINES = [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8,
        0, 3, 6,
        1, 4, 7,
        2, 5, 8,
        0, 4, 8,
        2, 4, 6
    ]

    def __init__(self):
        self.tiles = np.zeros([9])
        self.player = Game.PLAYER_1
        self.winner = None

        self.zobrist = Hash(9, 2)

    def board_tensor(self):
        result = np.zeros([2, 3, 3])
        for i, v in enumerate(self.tiles):
            if v == 0:
                continue
            index = 0 if v == self.current_player else 1
            result[index, i % 3, i // 3] = 1
        return result
    
    def current_player(self):
        return self.player
    
    def legal_actions(self, one_hot = False):
        if one_hot:
            actions = np.zeros([9])
            for i, val in enumerate(self.tiles):
                if val == 0:
                    actions[i] = 1
            return actions

        else:
            actions = set()
            for i, val in enumerate(self.tiles):
                if val == 0:
                    actions.add(i)
            return list(actions)
    
    def legal_action(self, action):
        if action < 0 or action > 8:
            return False
        return self.tiles[action] == 0

    def check_winner(self):
        for i in range(0, 24, 3):
            index = i
            win = True
            for j in range(3):
                if self.tiles[self.LINES[index]] != self.player:
                    win = False
                    break
                index += 1

            if win == False:
                continue

            self.winner = self.player
            return self.winner

        for tile in self.tiles:
            if tile == 0:
                return self.winner
        
        self.winner = Game.TIE
        return self.winner

    def apply_action(self, action):
        self.tiles[action] = self.player
        self.check_winner()

        if self.player == Game.PLAYER_1:
            self.zobrist.apply_action(action, 0)
            self.player = Game.PLAYER_2
        else:
            self.zobrist.apply_action(action, 1)
            self.player = Game.PLAYER_1

        return self
    
    def game_finished(self):
        return self.winner is not None

    def copy(self):
        result = Tictactoe_State()
        
        result.tiles = np.copy(self.tiles)
        result.player = self.player
        result.winner = self.winner

        result.zobrist = self.zobrist.copy()

        return result
    
    def __hash__(self):
        return self.zobrist.hash()