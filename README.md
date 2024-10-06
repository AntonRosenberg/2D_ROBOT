# 2D_ROBOT

The 2D_ROBOT project implements two A* algorithms for pathfinding in a 2D space with obstacles. The algorithms calculate either the shortest distance or the shortest time path from a starting point to a goal while avoiding obstacles. It is assumed for both cases that the robot can touch the obstacles but not go inside of them.
Similarly the robot can touch the boundaries but not go outside of them. For example if an obstacle touches the boundar

## Features

- **Two A* Algorithms**:
  - Shortest Distance A*
  - Shortest Time A*

- **Input Format**: 
  - The program takes an input YAML file that defines the starting point, goal, space size, and obstacles.

- **Plotting**:
  - Use the `--plot` flag to visualize the path and obstacles.

## Prerequisites

-   You need to have pip and python3.xx-venv installed

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd 2D_ROBOT

2.  Start an virtual environment:  
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate

4.  Install required third party libraries: 
    ```bash
    pip install -r requirements.txt

5.  Make sure it's installed correctly by running the tests
    ```bash
    pytest

## Usage

- **Run the program using this command**
- python main.py <input_yaml_file>  --plot -type <distance|time> 

- <input_yaml_file>: Path to the YAML file containing the configuration for the pathfinding.
- --plot: (Optional) Flag to generate a plot of the path and obstacles.
- -type <distance|time>: (default: distance) Specify whether to use the shortest distance or shortest time A* algorithm.

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
