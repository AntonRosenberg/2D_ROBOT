# A* Algorithm Implementation
import heapq
import numpy as np


def reconstruct_path(came_from, current):
    """Reconstruct path from start to goal."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def a_star_dist(graph, start, goal):
    """Preform A* search on graph using distance as cost"""
    def heuristic(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5  # Euclidean distance

    open_set = []
    heapq.heappush(open_set, (0, tuple(start)))
    came_from = {}
    g_score = {tuple(start): 0}
    f_score = {tuple(start): heuristic(start, goal)}
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == tuple(goal):
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + heuristic(current, neighbor)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return []  # Return empty path if no path found


###################################################################

def a_star_kinematic(graph, start, goal, kinematics_model):
    """Perform A* search on the graph with time as costs, including penalty for turns."""
    
    def heuristic(node, goal, acceleration, velocity):
        """Heuristic function: Time-based estimate (using distance and velocity)."""
        distance = np.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)
        return (np.sqrt(velocity**2 + 2 * acceleration * distance) - velocity) / acceleration

    # Priority queue for A* search (f_score, current_node, previous_node, velocity)
    open_set = []
    heapq.heappush(open_set, (0, start, None, kinematics_model.velocity))
    
    # Dictionaries to track the optimal path
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    # Track velocities at each node
    v_score = {node: float('inf') for node in graph}
    v_score[start] = kinematics_model.velocity
    
    # Estimated time to goal (f_score)
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal, kinematics_model.acceleration, kinematics_model.velocity)
    
    while open_set:
        # Get the node with the lowest f_score
        current_f, current, prev_node, current_velocity = heapq.heappop(open_set)
        
        # If we've reached the goal, reconstruct the path
        if current == goal:
            return reconstruct_path(came_from, goal)
        
        # Explore each neighbor of the current node
        for neighbor in graph[current]:
            # Update the kinematics model velocity based on the current velocity
            kinematics_model.velocity = current_velocity
            
            # Calculate the time to traverse from current to neighbor and update the velocity
            time_to_neighbor = kinematics_model.time_to_traverse(current, neighbor, prev_node)
            final_velocity = kinematics_model.velocity  # Final velocity at the neighbor after traversal
            
            # Calculate tentative g_score for this neighbor
            tentative_g_score = g_score[current] + time_to_neighbor
            
            # If this path to neighbor is better (lower g_score), update the path
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                v_score[neighbor] = final_velocity  # Update the velocity at the neighbor
                
                # Calculate the f_score (g_score + heuristic)
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal, kinematics_model.acceleration, final_velocity)
                
                # Push the neighbor to the open set with its f_score, neighbor, current node, and final velocity
                heapq.heappush(open_set, (f_score[neighbor], neighbor, current, final_velocity))
    
    # No path found
    return []

