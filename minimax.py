from tictactoe import checkWinner, turnChange
import numpy as np

def minimax(board, turn, scoreList=[], moveList=[]):
    state = checkWinner(board)
    if state == 'draw': return 0, None
    elif state == 'o': return 1, None
    elif state != -1: return -1, None

    scoreList = []
    moveList = []

    for y in range(3):
        for x in range(3):  
            if board[y][x] == ' ': 

                boardCopy = [layer[:] for layer in board]
                boardCopy[y][x] = turn
                scoreList.append(minimax(boardCopy, turnChange(turn)))
                moveList.append((y*3)+x+1)
    
    if turn == 'o':
        scores = [score[0] for score in scoreList]
        return max(scores), moveList[np.argmax(scores)]
    else:
        scores = [score[0] for score in scoreList]
        return min(scores), moveList[np.argmin(scores)]