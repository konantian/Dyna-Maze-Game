"""
  Purpose: For use in the Reinforcement Learning course, Fall 2018,
  University of Alberta.
  Gambler's problem environment using RLGlue.
"""
from rl_glue import BaseEnvironment
import numpy as np


class Environment(BaseEnvironment):

    def __init__(self):
        """Declare environment variables."""

    def env_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize environment variables necessary for run.
        """
        self.state=None
        self.wall=set([(2,1),(2,2),(2,3),(5,4),(7,0),(7,1),(7,2)])

    def env_start(self):
        """
        Arguments: Nothing
        Returns: state - numpy array
        Hint: Sample the starting state necessary for exploring starts and return.
        """

        #Set the start state

        self.state=(0,2)
        return self.state

    def env_step(self, action):
        """
        Arguments: action - integer
        Returns: reward - float, state - numpy array - terminal - boolean
        Hint: Take a step in the environment based on dynamics; also checking for action validity in
        state may help handle any rogue agents.
        """
        #calculate next state based on the action taken
        testState=tuple(map(sum,zip(self.state,action)))
        x,y=testState

        if  testState not in self.wall and 0<=x<=8 and 0<=y<=5:

            self.state = testState

            if self.state == (8, 0):
                return 1,self.state,True

        return 0,self.state,False

    def env_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: response based on in_message
        This function is complete. You do not need to add code here.
        """
        if in_message == "return":
            return self.state
