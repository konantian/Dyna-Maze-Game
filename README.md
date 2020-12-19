# Dyna-Maze-Game
## Reinforcement learning Second edition Chapter8 Example 8.1 implementation
[agentMaze.py](https://github.com/konantian/Dyna-Maze-Game/blob/master/Codes/agentMaze.py) This file is for learning and generate action under specific state<br />

[envMaze.py](https://github.com/konantian/Dyna-Maze-Game/blob/master/Codes/envMaze.py) This is the environmnet for this problem, given an action under a state, return the next state<br />

[expMaze.py](https://github.com/konantian/Dyna-Maze-Game/blob/master/Codes/expMaze.py) This is main file to run this project and has interaciton with RLGlue model and pygame to display the progress.

[rl_glue.py](https://github.com/konantian/Dyna-Maze-Game/blob/master/Codes/rl_glue.py) This is the file contains maze implementation by pygame and the Rlglue framework for Reinforcement learning.

## Getting Started
The following instructions will get you a copy of this project and you can run the project on your local machine or you can try the demo without any setup

How to start
------------
1. Clone this project: `git clone https://github.com/konantian/Dyna-Maze-Game.git`
2. Enter the project: `cd Dyna-Maze-Game/Codes`
3. Start the game: 
```shell
python3 expMaze.py 5 (5 is for n and you can modify this by yourself)
```

### Prerequisites
You need to install the following software:

* Python3

* pygame

### Installation
> Install the package for python

```shell
$ pip install -r requirements.txt
```

## Problem Description
 Consider the simple maze shown inset in Figure 8.2. In
each of the 47 states there are four actions, up, down, right, and left, which take the
agent deterministically to the corresponding neighboring states, except when movement
is blocked by an obstacle or the edge of the maze, in which case the agent remains where
it is. Reward is zero on all transitions, except those into the goal state, on which it is +1.
After reaching the goal state (G), the agent returns to the start state (S) to begin a new
episode. This is a discounted, episodic task with </p>
 <br>The main part of Figure 8.2 shows average learning curves from an experiment in
which Dyna-Q agents were applied to the maze task. The initial action values were zero,
the step-size parameter was ↵ = 0.1, and the exploration parameter was " = 0.1. When
selecting greedily among actions, ties were broken randomly. The agents varied in the
number of planning steps, n, they performed per real step. For each n, the curves show
the number of steps taken by the agent to reach the goal in each episode, averaged over 30
repetitions of the experiment. In each repetition, the initial seed for the random number
generator was held constant across algorithms. Because of this, the first episode was
exactly the same (about 1700 steps) for all values of n, and its data are not shown in
the figure. After the first episode, performance improved for all values of n, but much
more rapidly for larger values. Recall that the n = 0 agent is a nonplanning agent, using
only direct reinforcement learning (one-step tabular Q-learning). This was by far the
slowest agent on this problem, despite the fact that the parameter values (↵ and ") were
optimized for it. The nonplanning agent took about 25 episodes to reach ("-)optimal
performance, whereas the n = 5 agent took about five episodes, and the n = 50 agent
took only three episodes.</p>
## The screenshot of running progress
![alt text](https://github.com/konantian/Dyna-Maze-Game/blob/master/Images/DynaMaze.png)

## The background algorithm from "Reinforcement learning Second edition"
![alt text](https://github.com/konantian/Dyna-Maze-Game/blob/master/Images/Algorithm.png)

## The performance plot for n=0, 5 and 50
![alt text](https://github.com/konantian/Dyna-Maze-Game/blob/master/Images/plot.png)

## Compare between no-planning and planning
![alt text](https://github.com/konantian/Dyna-Maze-Game/blob/master/Images/planning.png)
