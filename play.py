from game import Game

class Play:

    def __init__(self, game, player_1, player_2):
        self.game = game
        self.player_1 = player_1
        self.player_2 = player_2

        self.current_state = None
        self.state_history = None

    def play_game(self):
        self.current_state = self.game.starting_state()
        self.state_history = [self.game.copy(self.current_state)]

        while not self.game.game_finished(self.state_history):

            if self.game.current_player(self.current_state) == Game.PLAYER_1:
                action = self.player_1.get_action(self.state_history)
                self.current_state = self.game.next_state(self.state_history, action)
            else:
                action = self.player_2.get_action(self.state_history)
                self.current_state = self.game.next_state(self.state_history, action)
            
            self.state_history.append(self.game.copy(self.current_state))

        return self.game.winner(self.state_history)
    
    def play_games(self, n):
        player_1_win    = 0
        player_2_win    = 0
        tie             = 0

        for _ in range(n // 2):
            result = self.play_game()

            if result == Game.PLAYER_1:
                player_1_win += 1
            elif result == Game.PLAYER_2:
                player_2_win += 1
            else:
                tie += 1
        
        self.player_1, self.player_2 = self.player_2, self.player_1

        for _ in range(n // 2):
            result = self.play_game()

            if result == Game.PLAYER_1:
                player_2_win += 1
            elif result == Game.PLAYER_2:
                player_1_win += 1
            else:
                tie += 1
        
        self.player_1, self.player_2 = self.player_2, self.player_1

        return player_1_win, player_2_win, tie