# 2D_ROBOT

The 2D_ROBOT project implements two A* algorithms for pathfinding in a 2D space with obstacles. The algorithms calculate either the shortest distance or the shortest time path from a starting point to a goal while avoiding obstacles.

## Features

- **Two A* Algorithms**:
  - Shortest Distance A*
  - Shortest Time A*

- **Input Format**: 
  - The program takes an input YAML file that defines the starting point, goal, space size, and obstacles.

- **Plotting**:
  - Use the `--plot` flag to visualize the path and obstacles.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd 2D_ROBOT

2. pip install -r requirements.txt

## Usage
- python main.py <input_yaml_file> --plot -type <distance|time>

- Here is an example of how the YAML input file should be structured:
    x_start: 2 
    y_start: 2
    x_goal: 98
    y_goal: 98
    x_space_size: 100
    y_space_size: 100
    list_obstacles: [
        [[5,5], [10,5], [8,12]],
        [[50,60], [70,40], [80,90], [60,80]]
    ]



