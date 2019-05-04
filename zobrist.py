import random

class Hash:
    KEYS = []
    ACTION_SPACE_SIZE = 0
    NUM_PEICES = 0

    INIT = False

    @staticmethod
    def generate_keys(action_space_size, num_peices):
        Hash.ACTION_SPACE_SIZE = action_space_size
        Hash.NUM_PEICES = num_peices
        Hash.KEYS = [0] * (action_space_size * num_peices)
        for i in range(action_space_size * num_peices):
            Hash.KEYS[i] = int(random.getrandbits(8 * 4))

    def __init__(self, action_space_size = None, num_peices = None):
        if Hash.INIT == False:
            assert(action_space_size is not None)
            assert(num_peices is not None)

            Hash.INIT = True
            Hash.generate_keys(action_space_size, num_peices)

        self.h = 0

    def apply_action(self, action, peice):
        self.h ^= Hash.KEYS[action + Hash.ACTION_SPACE_SIZE * peice]
    
    def copy(self):
        result = Hash()
        result.h = self.h

        return result

    def hash(self):
        return self.h