from random import choice
from math import log, sqrt

# Todo: Add policy from nnet weight to simulation action priority
class MCTS:
    def __init__(self, game, nnet, simulations = 800, c = 1.4):
        self.game = game
        self.nnet = nnet
        self.simulations = simulations

        self.wins = {}
        self.plays = {}

        self.c = c

        self.state_history = []

    def get_play(self, state_history, verbose = False):
        self.state_history = state_history

        state = self.state_history[-1]
        actions = self.game.legal_actions(self.state_history)

        if actions is None:
            return None
        if len(actions) == 0:
            return None
        if len(actions) == 1:
            return actions[0]

        player = self.game.current_player(state)

        for _ in range(self.simulations):
            self.run_simulation()

        states = [self.game.next_state(self.state_history, a) for a in actions]
        keys = [self.game.string(s) for s in states]

        action, percent_wins = None, None

        for i in range(len(actions)):
            a, k = actions[i], keys[i]
            if k in self.plays:
                p_w = self.wins[k] / self.plays[k]
                if action is None or p_w > percent_wins:
                    action, percent_wins = a, p_w
                if verbose:
                    print('Action: {}, Percent Wins: {:.2f}.'.format(a, p_w))
        
        return action

    def run_simulation(self):
        visited = set()

        history_copy = self.state_history[:]
        root_player = self.game.current_player(self.state_history[-1])

        
        while True:
            actions = self.game.legal_actions(history_copy)
            states = [self.game.next_state(history_copy, a) for a in actions]
            keys = [self.game.string(s) for s in states]
            players = [self.game.current_player(s) for s in states]

            i = None

            # If all child nodes have values, calculate UCB1
            # Otherwise, pick one that hasn't been visited
            if all(self.plays.get(k) for k in keys):

                log_total = log(sum(self.plays[k] for k in keys))
                value = None
                for j, k in enumerate(keys):
                    v = self.wins[k] / self.plays[k] + self.c * sqrt(log_total / self.plays[k])
                    if i is None or v > value:
                        i, value = j, v

            else:

                indices = [j for j, k in enumerate(keys) if k not in self.plays]
                i = choice(indices)
            
            a, s, k, p = actions[i], states[i], keys[i], players[i]

            history_copy.append(s)
            visited.add((a, s, k, p))

            if k not in self.plays:
                self.plays[k] = 0
                self.wins[k] = 0
                break
            
            if self.game.game_finished(history_copy):
                break
        
        # V is from the root player's perspective
        v = None
        if self.game.game_finished(history_copy):
            v = root_player * self.game.winner(history_copy)    
        else:
            v, _ = self.nnet.predict(history_copy, root_player)
        v = (v + 1) / 2

        for a, s, k, p in visited:
            self.plays[k] += 1
            if root_player == p:
                self.wins[k] += 1 - v
            else:
                self.wins[k] += v