import math
from shapely.geometry import LineString, Polygon

'''
def line(point1, point2):
    space = [min(point1[0], point2[0]), max(point1[1], point2[1])]
    if point1[0] != point2[0]:
        k = (point2[1] - point1[1])/(point2[0] - point1[0])
        m = point1[1] - k*point1[0]
    else:
        k = math.inf
        m = math.inf

    return k, m, space


def intersects(point1, point2, polygon):
    k, m, space = line([point1, point2])
    segments = polygon.xy
    for i in range(len(segments)):
        ...
'''

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
            if line.intersects(polygon) and not (line.touches(polygon) and not line.within(polygon)):
                return False
        return collision