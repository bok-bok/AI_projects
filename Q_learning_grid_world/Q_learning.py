import numpy as np
row = 5
col = 5
from environment import State

class Agent:
    def __init__(self):
        self.State = State()
        self.actions = ["left", "down", "right","up"]
        self.states =[]
        self.Q_table = {}
        self.learning_rate = 0.2
        self.exp_line = 0.3
        for i in range(row):
            for j in range(col):
                self.Q_table[(i,j)] = {}
                for a in self.actions:
                    self.Q_table[(i,j)][a] = 0


    def choose_action(self):
        action = ""
        if np.random.uniform(0,1) < self.exp_line:
            action = np.random.choice(self.actions)
        else:
            mx_reward = 0
            for a in self.actions:
                reward = self.Q_table[self.State.state][a]
                if reward >= mx_reward:

                    mx_reward =reward
                    action = a
        return action

    def take_action(self,action):
        new_state = self.State.next_position(action)

        return State(position=new_state)

    def reset(self):
        self.states = []
        self.State = State()

    def play(self, rounds = 10):
        i = 0
        while(i < rounds):
            if self.State.end:
                reward = self.State.get_reward()

                for s in reversed(self.states):
                    q_table = self.Q_table[s[0]][s[1]]
                    reward = q_table + self.learning_rate*(reward - q_table)
                    self.Q_table[s[0]][s[1]] = round(reward,3)

                self.reset()
                i += 1
            else:
                while(True):
                    now = self.State.state
                    action = self.choose_action()
                    next = self.State.next_position(action)
                    if(now != next):
                        break

                self.states.append([self.State.state, action])
                self.State = self.take_action(action)

                self.State.is_end()









ag = Agent()
rounds = int(input("how many games do you want to iterate to educate your bot?: "))
ag.play(rounds)
print("printing Q_table -------------------------")
print(ag.Q_table)












