import random
from Othello import *

class Player(BasePlayer):
    def __init__(self, timeLimit):
        BasePlayer.__init__(self, timeLimit)
        self.maxDepth = 4

    def findMove(self, state):
        bestMove = None
        bestValue = float('-inf')

        # Loop through all possible moves
        for move in state.actions():
            nextState = state.result(move)
            value = self.alphabeta(nextState, self.maxDepth - 1,
                                   float('-inf'), float('inf'), False)
            if value > bestValue:
                bestValue = value
                bestMove = move

        print(f"AI chooses move: {state.moveToStr(bestMove)} (value: {bestValue})")
        self.setMove(bestMove)

    def alphabeta(self, state, depth, alpha, beta, maximizingPlayer):
        
        # Stop if depth limit reached or game is over
        if depth == 0 or state.gameOver():
            return self.heuristic(state)

        if maximizingPlayer:
            value = float('-inf')
            for move in state.actions():
                nextState = state.result(move)
                value = max(value, self.alphabeta(nextState, depth-1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  # Beta cut-off
            return value
        else:
            value = float('inf')
            for move in state.actions():
                nextState = state.result(move)
                value = min(value, self.alphabeta(nextState, depth-1, alpha, beta, True))
                beta = min(beta, value)
                if alpha >= beta:
                    break  # Alpha cut-off
            return value

    def heuristic(self, state):
       return state.score()
