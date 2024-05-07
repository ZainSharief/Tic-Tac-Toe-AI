from minimax import minimax
from tictactoe import *
import random

def main():

    board = [
        [' ', ' ', ' '], 
        [' ', ' ', ' '], 
        [' ', ' ', ' ']
    ]

    turn = random.choice(['x', 'o'])
    playing = True

    while playing:
        display(board)

        if turn == 'x':
            valid = False
            while not valid:
                pos = int(input('Enter where you would like to play: (1-9): '))
                board, valid = move(board, turn, pos)

        else:
            print('AI to play: ')
            score, bestmove = minimax(board, turn)
            board, valid = move(board, turn, bestmove)

        turn = turnChange(turn)

        outcome = checkWinner(board)
        if outcome != -1:
            playing = False
            display(board)

        if outcome == 'x' or outcome == 'o':
            print(outcome + ' Wins!')
        elif outcome == 'draw':
            print('The game is a draw!')

if __name__ == '__main__':
    main()