import numpy as np

class KinematicsModel:
    def __init__(self, acceleration):
        self.acceleration = acceleration
        self.velocity = 0
    
    def time_to_traverse(self, p1, p2, prev_vertex=None):
        """
        Calculate time to traverse the edge from p1 to p2.
        If there is a previous segment, consider the angle between the two segments for deceleration.
        """
        distance = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        if prev_vertex:
            angle = self.calculate_angle(p1, p2, prev_vertex)
        else:
            angle = 0
        vf = self.velocity*np.cos(angle)
        v1 = np.sqrt((self.acceleration*distance+self.velocity**2+vf**2)/2)
        t_tot = (2*v1 - self.velocity - vf)/self.acceleration
        self.velocity = vf
        return t_tot

    def calculate_angle(self, p0, p1, p2):
        """
        Calculate the penalty based on the angle between the two segments: p0->p1 and p1->p2.
        Sharper turns incur more deceleration.
        """
        # Vector p0->p1
        v1 = (p1[0] - p0[0], p1[1] - p0[1])
        # Vector p1->p2
        v2 = (p2[0] - p1[0], p2[1] - p1[1])
        
        # Calculate the angle between v1 and v2 using the dot product
        dot_product = v1[0] * v2[0] + v1[1] * v2[1]
        mag_v1 = np.sqrt(v1[0]**2 + v1[1]**2)
        mag_v2 = np.sqrt(v2[0]**2 + v2[1]**2)
        
        # Cosine of the angle
        cos_theta = dot_product / (mag_v1 * mag_v2)
        
        # Angle in radians
        angle = np.acos(cos_theta)
        return angle
