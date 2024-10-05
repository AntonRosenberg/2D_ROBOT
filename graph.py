class Graph:
    def __init__(self, robotMap):
        self.robotMap = robotMap
        self.graph = {}
        self.vertices = self.get_vertices()
        self.construct_graph()
    
    def get_vertices(self):
        """Get all vertices from obstacles, including start and goal points, only if they are within bounds."""
        vertices = [self.robotMap.start, self.robotMap.goal]
        for obstacle in self.robotMap.obstacles:
            for vertex in obstacle.exterior.coords[:-1]:  # Exclude repeated last vertex
                if self.robotMap.is_inbounds(vertex):
                    vertices.append(vertex)
        return vertices
    
    def construct_graph(self):
        """Construct the visibility graph by connecting all visible vertices."""
        for i, v1 in enumerate(self.vertices):
            self.graph[v1] = []
            for j, v2 in enumerate(self.vertices):
                if i != j and self.robotMap.is_collision_free(v1, v2):
                    self.graph[v1].append(v2)
