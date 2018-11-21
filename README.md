# Dyna-Maze-Game
## Reinforcement learning Second edition Chapter8 Example 8.1 implementation
[agentMaze.py](https://github.com/konantian/Dyna-Maze-Game/blob/master/agentMaze.py) This file is for learning and generate action under specific state
[envMaze.py](https://github.com/konantian/Dyna-Maze-Game/blob/master/envMaze.py) This is the environmnet for this problem, given an action under a state, return the next state
[expMaze.py](https://github.com/konantian/Dyna-Maze-Game/blob/master/expMaze.py) This is main file to run this project and has interaciton with RLGlue model and pygame to display the progress.

Before start
------------
```
pygame
python3
```

How to start
------------
1. Clone this project: `git clone https://github.com/konantian/Dyna-Maze-Game.git`
2. Enter the project: `cd Dyna-Maze-Game`
3. Start the game: `python3.6 expMaze.py 5 (5 is for n and you can modify this by yourself)`

## Problem Description
Consider the simple maze shown inset in Figure 8.2. In
each of the 47 states there are four actions, up, down, right, and left, which take the
agent deterministically to the corresponding neighboring states, except when movement
is blocked by an obstacle or the edge of the maze, in which case the agent remains where
it is. Reward is zero on all transitions, except those into the goal state, on which it is +1.
After reaching the goal state (G), the agent returns to the start state (S) to begin a new
episode. This is a discounted, episodic task with 
## The screenshot of running progress
![alt text](https://github.com/konantian/Dyna-Maze-Game/blob/master/DynaMaze.png)

## The background algorithm from "Reinforcement learning Second edition"
![alt text](https://github.com/konantian/Dyna-Maze-Game/blob/master/Algorithm.png)

## The performance plot for n=0, 5 and 50
![alt text](https://github.com/konantian/Dyna-Maze-Game/blob/master/plot.png)

## Compare between no-planning and planning
![alt text](https://github.com/konantian/Dyna-Maze-Game/blob/master/planning.png)
