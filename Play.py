from Othello import *

import sys, importlib, argparse, time

def play(player1, player2, timeLimit, graphicsSize):
    state = Othello(numpy.array([Othello.black0, Othello.white0], dtype=numpy.uint64))
    if g is not None:
        g.draw(state)

    moveSequence = []

    while not state.gameOver():
        print(state)

        if state.getTurn() % 2 == 0:
            player1._startTime = time.time()
            player1.findMove(state)
            move = player1.getMove()
            print(f'Black moves {state.moveToStr(move)}\n')
        else:
            player2._startTime = time.time()
            player2.findMove(state)
            move = player2.getMove()
            print(f'White moves {state.moveToStr(move)}\n')
        state = state.result(move)
        moveSequence.append(move)

        if g is not None:
            g.draw(state)

        print(f'Discs:   \t{state.count(0)}\t{state.count(1)}')
        print(f'Stable: \t{state.stable(0)}\t{state.stable(1)}')
        print(f'Mobile: \t{state.mobility(0)}\t{state.mobility(1)}')
        print(f'Frontier:\t{state.frontier(0)}\t{state.frontier(1)}')
        print(f'Corner: \t{state.corner(0)}\t{state.corner(1)}')
        print()

    print(state)
    if state.winner() == 0:
        print('Black wins!')
        print(state.count(0), 'to', state.count(1))
    elif state.winner() == 1:
        print('White wins!')
        print(state.count(1), 'to', state.count(0))
    else:
        print("It's a draw")

    print()
    print('Moves', ' '.join(state.moveToStr(x) for x in moveSequence))

    print()
    print('Black player stats:')
    player1.stats()
    print()
    print('White player stats:')
    player2.stats()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description ='Play Othello')
    parser.add_argument('player1', type=str)
    parser.add_argument('player2', type=str)
    parser.add_argument('time_limit', type=float, help="time to make a move")
    parser.add_argument('-g', type=int, help="size of graphics window")
    args = parser.parse_args()

    try:
        player1Module = importlib.import_module(args.player1.split('.')[0])
    except:
        print('Invalid player 1 module')
        sys.exit()
    try:
        player2Module = importlib.import_module(args.player2.split('.')[0])
    except:
        print('Invalid player 2 module')
        sys.exit()

    timeLimit = args.time_limit
    player1 = player1Module.Player(timeLimit)
    player2 = player2Module.Player(timeLimit)

    if args.g:
        from Graphics import *
        player1name = args.player1.split('.')[0].split('/')[-1]
        player2name = args.player2.split('.')[0].split('/')[-1]
        g = Graphics(args.g, player1name, player2name)
    else:
        g = None

    play(player1, player2, timeLimit, g)
