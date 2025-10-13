import random
from Othello import *

class Player(BasePlayer):
    def __init__(self, timeLimit):
        BasePlayer.__init__(self, timeLimit)

    def findMove(self, state):
        actions = state.actions()
        self.setMove(random.choice(actions))
