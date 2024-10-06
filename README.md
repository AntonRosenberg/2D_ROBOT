# 2D_ROBOT

The 2D_ROBOT project implements two A* algorithms for pathfinding in a 2D space with obstacles. The algorithms calculate either the shortest distance or the shortest time path from a starting point to a goal while avoiding obstacles. It is assumed that the robot can touch the obstacles but not go inside of them. The robot has to be within the boundaries at all times i.e. if a boundary is at x=100 the robots x position x_r has to be < 100.

If there is no possible solution or if any obstacle intersects with itself the program will rasie an exception.

When calculating the shortest time the program makes the following assumptions:
- The robot has a constant acceleration which can be applied in any direction
- The robot has no set maximum velocity
- Turning is penalised through a deacceleration factor which depends on steepnes of the curve (penalty is a factor in [0, 1] to the final velocity of the segment)

## Features

- **Two A-star Algorithms**:
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
    git clone https://github.com/AntonRosenberg/2D_ROBOT.git
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

- **Run the program**
    ```bash
    python main.py <input_yaml_file>  --plot -type <distance|time> 

- **<input_yaml_file>** 
    - Path to the YAML file containing the configuration for the pathfinding.
- **--plot** 
    - (Optional) Flag to generate a plot of the path and obstacles.
- **-type <distance|time>**
    - (default: distance) Specify whether to use the shortest distance or shortest time A-star algorithm.

- **Here is an example of how the YAML input file should be structured**
    ```bash
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

## Testing and Continuous Integration

This project uses **pytest** for running unit tests and **GitHub Actions** for continuous integration.

[![Python Tests](https://github.com/AntonRosenberg/2D_ROBOT/blob/main/.github/workflows/ci.yml)](https://github.com/AntonRosenberg/2D_ROBOT/actions)