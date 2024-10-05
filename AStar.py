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

def heuristic(node, goal, acceleration, velocity):
    """Heuristic function: Time-based estimate (using distance and max acceleration)."""
    distance = np.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)
    return (np.sqrt(velocity**2+2*acceleration*distance)-velocity)/acceleration

def a_star_with_turns(graph, start, goal, kinematics_model):
    """Perform A* search on the graph with time-based costs, including turns."""
    
    # Priority queue for A* search
    open_set = []
    heapq.heappush(open_set, (0, start, None))  # (f_score, node, previous_node)
    
    # Dictionaries to track the optimal path
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal, kinematics_model.acceleration)
    
    while open_set:
        current_f, current, prev_node = heapq.heappop(open_set)
        
        # If we've reached the goal, reconstruct the path
        if current == goal:
            return reconstruct_path(came_from, goal)
        
        # Explore neighbors
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + kinematics_model.time_to_traverse(current, neighbor, prev_node, kinematics_model.acceleration, max_deceleration)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal, kinematics_model.acceleration, kinematics_model.velocity)
                heapq.heappush(open_set, (f_score[neighbor], neighbor, current))
    
    return None  # No path found

