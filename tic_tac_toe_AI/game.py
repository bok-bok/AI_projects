import pickle
import numpy as np

ROW = 3
COL = 3

class State:
    def __init__(self,p1,p2):
        self.board = np.zeros(ROW,COL)
        self.p1 = p1
        self.p2 = p2
        self.end = False
        self.boardHash = None

        self.playerSymbol = 1


    # get unique hash of current board state
    def getHash(self):
        self.boardHash = str(self.board.reshape(COL*ROW))
        return self.boardHash


    def winner(self):
        win = [[(0, 0), (0, 1), (0, 2)],
               [(1, 0), (1, 1), (1, 2)],
               [(2, 0), (2, 1), (2, 2)],
               [(0, 0), (1, 0), (2, 0)],
               [(0, 1), (1, 1), (2, 1)],
               [(0, 2), (1, 2), (2, 2)],
               [(0, 0), (1, 1), (2, 2)],
               [(0, 2), (1, 1), (2, 0)]]
        for combination in win:
            play1 = 0
            play2 = 0
            for r, c in combination:
                if self.board[r][c] == 1:
                    play1 += 1
                elif self.board[r][c] == 0:
                    play2 += 1
            if play1 == 3:
                return -1
            elif play2 == 3:
                return 1
        return None



    def avaiablePosition(self):
        position = []
        for i in range(ROW):
            for j in range(COL):
                if self.board[i][j] == 0:
                    position.append((i,j))

        return position



    def updateState(self,position):
        self.board[position] = self.playerSymbol
        self.playerSymbol = 1 if self.playerSymbol == 1 else -1


















