#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import numpy as np
import yaml
import argparse
from RobotMap import RobotMap
from graph import Graph
from AStar import a_star_dist

def main():
    parser = argparse.ArgumentParser(prog='shortestPathFinding', description='Find the Shortest Path that avoids obstacles')
    parser.add_argument('inputyaml')
    parser.add_argument('output', nargs='?', default='solution.txt')
    parser.add_argument('--plot', action='store_true')
    args = parser.parse_args()
    # Load input
    indata = yaml.load(open(args.inputyaml), yaml.Loader)
    obstacles = indata['list_obstacles']
    start = (indata['x_start'], indata['y_start'])
    goal = (indata['x_goal'], indata['y_goal'])
    size = (indata['x_space_size'], indata['y_space_size']) 

    # Create a map with start, goal, bounds/size and obstacles
    robotMap = RobotMap(start, goal, size, obstacles)
    # Use the map to create a graph with where start goal and the verticies of the obsticles are
    # the verticies in the graph.
    graph = Graph(robotMap)
    # Run A-star algorithm to find shortest path
    path = a_star_dist(graph.graph, start, goal)
    if not path:
        raise Exception("No valid path from start to goal found")
    print(path)
    path = np.array(path)

    # Visualize
    if args.plot:
        fig, ax = plt.subplots()
        for obstacle in obstacles:
            p = patch.Polygon(np.array(obstacle))
            print(p)
            ax.add_patch(p)
        if len(path) != 0:
            ax.plot(path[:,0], path[:,1], 'r.-')
        ax.set_xlim([0, indata['x_space_size']])
        ax.set_ylim([0, indata['y_space_size']])
        plt.savefig('solution.png')
        plt.show()

if __name__=="__main__":
    main()
