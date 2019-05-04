from player import Player

class Human_Player(Player):

    def __init__(self, game, name = 'Human Player'):
        super(Human_Player, self).__init__(game, name)
    
    def get_action(self, state_history):
        action = None
        print(self.game.string(state_history[-1]))

        legal = self.game.legal_actions(state_history)
        print('Legal actions: {}'.format(' '.join(str(x) for x in legal)))

        while True:

            action = input('Select a move: ')
            
            if action == '':
                continue
            try:
                action = int(action)
            except ValueError:
                continue
            
            return action