import copy
new_board = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]]
X = "X"
O = "O"

def player(board):
    x = 0
    o = 0
    for r in board:
        for c in r:
            if c == X:
                x += 1
            elif c == O:
                o += 1

    if x > o:
        return O
    else:
        return X

def print_board(board):
    print("-------------")
    print("| "+board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("-------------")
    print("| "+board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | ")
    print("-------------")
    print("| "+board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | ")
    print("-------------")
def actions(board):
    possible_actions = set()
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if c == " ":
                possible_actions.add(i,j)
    return possible_actions

def result(board,action):
    nBoard = copy.deepcopy(board)
    p = player(board)
    nBoard[action[0]][action[1]] = p
    return nBoard


def winner(board):
    win = [[(0,0),(0,1),(0,2)],
           [(1,0),(1,1),(1,2)],
           [(2,0),(2,1),(2,2)],
           [(0,0),(1,0),(2,0)],
           [(0,1),(1,1),(2,1)],
           [(0,2),(1,2),(2,2)],
           [(0,0),(1,1),(2,2)],
           [(0,2),(1,1),(2,0)]]
    for combination in win:
        x = 0
        o = 0
        for r, c in combination:
            if board[r][c] == X:
                x+=1
            elif board[r][c] == O:
                o += 1
        if x == 3:
            return X
        elif o == 3:
            return O
    return None

def terminal(board):
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False

def utility(board):
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0

def minimax(board):
    if(terminal(board)):
        return utility(board)
