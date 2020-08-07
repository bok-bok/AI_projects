import numpy as np
from environment import State
col = 5
row = 5
start = (4,0)
win = (0,4)
lose = (1,4)
wall = [(1,2),(3,2)]


class Bot:
    def __init__(self):
        self.State = State()
        self.states = []
        self.state_values = {}
        self.actions = ["up", "down", "right", "down"]
        self.learning_rate = 0.2
        self.exp_line = 0.4
        for i in range(row):
            for j in range(col):
                self.state_values[i,j] = 0

    def get_reward(self):
        if self.State.state == win:
            return 1
        elif self.State.state == lose:
            return -1
        else:
            return 0

    def choose_action(self):
        action = ""
        mx_reward = 0
        if np.random.uniform(0,1) <= self.exp_line:
            action = np.random.choice(self.actions)
            return action
        else:
            # greedy action
            for a in self.actions:
                nx_reward = self.state_values[self.State.nxt_state(a)]
                if nx_reward >= mx_reward:
                    action = a
                    mx_reward = nx_reward
            return action

    def take_action(self,action):
        return State(self.State.nxt_state(action))



    def reset(self):
        self.State = State()
        self.states = []


    def game(self, num=10):
        i = 0
        while(i < num):
            if self.State.end:
                reward = self.get_reward()
                self.state_values[self.State.state] = reward
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.learning_rate*(reward - self.state_values[s])
                    self.state_values[s] = round(reward,3)
                i+=1
                self.reset()
            else:
                action = self.choose_action()
                self.State = self.take_action(action)
                self.states.append(self.State.state)


                self.State.is_end()

    def show(self):
        for i in range(0, row):
            print('----------------------------------')
            out = '| '
            for j in range(0, col):
                out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('----------------------------------')



ag = Bot()
counts = int(input("how many games do you want to educate your bot ?: "))
ag.game(counts)
print(ag.show())






















