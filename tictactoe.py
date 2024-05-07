def checkWinner(board):
    for i in range(0, 3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        
        elif board[0][i] != ' ' and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        
    if board[1][1] != ' ' and ((board[1][1] == board[0][0] == board[2][2]) or (board[1][1] == board[2][0] == board[0][2])):
        return board[1][1]
    
    for y in board:
        for x in y:
            if x == ' ': return -1
    
    return 'draw'
        
def turnChange(currentTurn):
    if currentTurn == 'o': return 'x' 
    else: return 'o'

def move(board, turn, pos):
    pos -= 1 
    layer = pos // 3
    position = pos % 3

    if board[layer][position] != ' ':
        print('Invalid Move, please try again...')
        return board, False 

    board[layer][position] = turn
    return board, True

def display(board):
    for y in board:
        print(y)
    print()
