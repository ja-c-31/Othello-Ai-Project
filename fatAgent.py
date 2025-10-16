from Othello import *

class Player(BasePlayer):
    def __init__(self, timeLimit):
        BasePlayer.__init__(self, timeLimit)

    def findMove(self, state):
        bestMove = None
        bestValue = float('-inf')

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
    
        if depth == 0 or state.isTerminal():
            return self.evaluate(state)

        if maximizingPlayer:
            value = float('-inf')
            for move in state.actions():
                nextState = state.result(move)
                value = max(value, self.alphabeta(nextState, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float('inf')
            for move in state.actions():
                nextState = state.result(move)
                value = min(value, self.alphabeta(nextState, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value

    def evaluate(self, state):
        
        black, white = state.countPieces()
        if self.color == 'black':
            return black - white
        else:
            return white - black
