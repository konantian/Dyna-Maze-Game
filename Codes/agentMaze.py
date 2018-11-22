"""
   Purpose: For use in the Reinforcement Learning course, Fall 2018,
   University of Alberta.
   Monte Carlo agent using RLGlue - barebones.
"""
from rl_glue import BaseAgent
import numpy as np
import random
import itertools

class MazeAgent(BaseAgent):

    def __init__(self,n):
        """Declare agent variables."""

        self.n=n
    def agent_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize the variables that need to be reset before each run
        begins
        Initialize the alpha,epsilon,all actions and Q
        """
        self.alpha=0.1
        self.gamma=0.95
        self.epsilon=0.1
        self.actions=["left","right","up","down"]
        self.coords=[(-1,0),(1,0),(0,1),(0,-1)]
        self.returns=dict(zip(self.actions,self.coords))
        L=list(itertools.product(range(9),range(6),self.actions))
        self.Q=dict(zip(L,len(L)*[0]))
        self.M={}
        self.visit={}
        self.action=None
        self.state=None

    def agent_start(self, state):
        """
        Arguments: state - numpy array
        Returns: action - integer
        Hint: Initialize the variables that you want to reset before starting
        a new episode, pick the first action, don't forget about exploring
        starts
        """
        x,y=state
        self.state=state
        self.action,coord=self._chooseAction(state)

        return coord

    def agent_step(self, reward, state):
        """
        Arguments: reward - floating point, state - numpy array
        Returns: action - integer
        Hint: select an action based on pi
        """

        x,y=self.state #S
        X,Y=state      #S'

        maxAction=self._calMax(state)

        self.Q[(x,y,self.action)]+=self.alpha*(reward+self.gamma*self.Q[(X,Y,maxAction)]-self.Q[(x,y,self.action)])

        if self.n != 0:
            self._planning(self.state,state,reward)

        self.action,coord=self._chooseAction(state)
        self.state=state

        return coord

    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        Hint: do necessary steps for policy evaluation and improvement
        """
        x,y=self.state

        self.Q[(x,y,self.action)]+=self.alpha*(reward-self.Q[(x,y,self.action)])

    def agent_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: The value function as a list.
        This function is complete. You do not need to add code here.
        """
        
        pass

    def calValue(self,state):

        x,y=state

        return np.mean([self.Q[(x,y,a)] for a in self.actions])

    def _chooseAction(self,state):

        action=np.random.choice(self.actions) if np.random.uniform(0,1) < self.epsilon else self._calMax(state)

        return action,self.returns[action]

    def _calMax(self,state):

        x,y=state
        values=[self.Q[x,y,action] for action in self.actions]
        greedy_actions=[action for action in self.actions if self.Q[(x,y,action)] == max(values)]

        return np.random.choice(greedy_actions)

    def _planning(self,previousState,currentState,reward):

        x,y=previousState
        X,Y=currentState

        if (x,y) in self.visit:
            self.visit[(x,y)].append(self.action)
        else:
            self.visit[(x,y)]=[self.action]

        self.M[(x,y,self.action)]=(reward,X,Y)

        for i in range(self.n):

            S=random.choice(list(self.visit.keys()))
            x,y=S

            randomActionList=self.visit[S]

            action=random.choice(randomActionList)

            R,X,Y=self.M[(x,y,action)]

            maxAction=self._calMax((X,Y))

            self.Q[(x,y,action)]+=self.alpha*(R+self.gamma*self.Q[(X,Y,maxAction)]-self.Q[(x,y,action)])

