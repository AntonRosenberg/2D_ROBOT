# A* Algorithm Implementation
import heapq


def a_star(graph, start, goal):
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
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(tuple(start))
            return path[::-1]  # Return reversed path
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + heuristic(current, neighbor)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return []  # Return empty path if no path found
