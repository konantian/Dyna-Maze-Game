# Dyna-Maze-Game
## Reinforcement learning Second edition Chapter8 Example 8.1 implementation

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
