class Game:

    PLAYER_1    =  1
    PLAYER_2    = -1
    TIE         =  0

    def __init__(self):
        pass
    
    def board_tensor_size(self):
        pass
    
    def status_tensor_size(self):
        # None if status tensor is not used
        pass
    
    def starting_state(self):
        pass
    
    def current_player(self, state):
        pass

    def legal_actions(self, state_history, one_hot = False):
        pass

    def legal_action(self, state_history, action):
        pass

    def next_state(self, state_history, action):
        pass
    
    def game_finished(self, state_history):
        pass
    
    def winner(self, state_history):
        pass
    
    def board_tensor(self, state, player = None):
        pass

    def status_tensor(self, state, player = None):
        pass

    def copy(self, state):
        pass

    def string(self, state):
        pass

    def hash(self, state):
        pass
    