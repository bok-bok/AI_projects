import numpy as np
col = 5
row = 5
start = (4,0)
win = (0,4)
lose = (1,4)
wall = [(1,2),(3,2)]
class State:
    def __init__(self, position = start):
        self.state = position
        self.board = np.zeros((row,col))
        self.board[wall[0]] = -1
        self.board[wall[1]] = -1
        self.end = False


    def nxt_state(self, action):
        r = self.state[0]
        c = self.state[1]

        if action == "up":
            next = (r-1,c)
        elif action == "down":
            next = (r+1,c)
        elif action == "right":
            next = (r, c+1)
        else:
            next = (r,c-1)
        if next[0] >= 0 and next[1] >= 0 and next[0] < row and next[1] < col:
            if self.board[next] != -1:
                return next

        return self.state

    def is_end(self):
        if self.state == win or self.state == lose:
            self.end = True
