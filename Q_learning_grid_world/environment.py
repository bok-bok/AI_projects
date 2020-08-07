import numpy as np
row = 5
col = 5
start = (4,0)
win = (0,4)
lose = (1,4)
class State:
    def __init__(self, position = start):
        self.state = position
        self.end = False


    def get_reward(self):
        if self.state == win:
            return 1
        elif self.state == lose:
            return -1
        else:
            return 0

    def next_position(self,action):
        r = self.state[0]
        c = self.state[1]
        if action == "up":
            next = (r-1,c)
        elif action == "down":
            next = (r+1, c)
        elif action == "right":
            next = (r,c+1)
        else:
            next = (r,c-1)
        if ((next[0] >= 0) and (next[1] >= 0) and (next[0] < row) and (next[1] < col)):
            return next
        return self.state


    def is_end(self):
        if self.state == win or self.state == lose:
            self.end = True


