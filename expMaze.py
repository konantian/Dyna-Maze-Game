"""
  Purpose: For use in the Reinforcement Learning course, Fall 2018, University of Alberta.
  Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlo agent using RLGlue.
"""
from rl_glue import RLGlue
from envMaze import Environment
from agentMaze import MazeAgent
import pygame
import numpy as np
import sys

def run(n):

    surface=create_window()
    #Set the experiment
    num_runs = 1
    maxEpisodes=50
    environment=Environment()
    agent=MazeAgent(n)
    rlglue=RLGlue(environment,agent,surface)
    rlglue.rl_init()
    np.random.seed(0)

    for i in range(maxEpisodes):
        rlglue.rl_episode()
        print(rlglue.num_ep_steps())

def create_window():

    title = "Dyna Maze"
    size = (550,370)
    pygame.init()
    surface = pygame.display.set_mode(size,0,0)
    pygame.display.set_caption(title)

    return surface

run(int(sys.argv[1]))


