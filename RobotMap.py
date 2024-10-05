from shapely.geometry import LineString, Polygon


class RobotMap:
    def __init__(self, start, goal, size, obstacles) -> None:
        self.start = start
        self.goal = goal
        self.size = size
        self.obstacles = []
        for obstacle in obstacles:
            polygon = Polygon(obstacle)
            if polygon.is_valid:
                self.obstacles.append(polygon)
            else:
                raise Exception("Invalid yaml input: obstacle intersects itself")

    def is_inbounds(self, point):
        x, y = point
        return 0 <= x <= self.size[0] and 0 <= y <= self.size[1]
    
    def is_collision_free(self, point1, point2):
        """Check if the line from point1 to point2 intersects any obstacle and stays within bounds."""
        if not self.is_inbounds(point1) or not self.is_inbounds(point2):
            return False
        collision = True
        line = LineString([point1, point2])
        for polygon in self.obstacles:
            # Check if line intersects any obstacle and if it does check that it doesn't go within
            # the obstacles borders.
            if line.intersects(polygon) and not (line.touches(polygon) and not line.within(polygon)):
                return False
        return collision