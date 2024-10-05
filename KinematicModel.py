import numpy as np

class KinematicsModel:
    def __init__(self, acceleration):
        self.acceleration = acceleration
        self.velocity = 0  # Initial velocity

    def time_to_traverse(self, p1, p2, prev_vertex=None):
        """
        Calculate time to traverse the edge from p1 to p2, factoring in deceleration based on the angle with the previous segment.
        """
        distance = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        if prev_vertex:
            # Calculate angle between the previous segment (prev_vertex -> p1) and the current segment (p1 -> p2)
            deceleration_factor = self.calculate_turn_based_deceleration(prev_vertex, p1, p2)
            vf = self.velocity * deceleration_factor  # Final velocity after deceleration from turn
        else:
            vf = self.velocity  # No deceleration if no previous segment

        # Calculate intermediate velocity (v1) and total time to traverse the segment
        v1 = np.sqrt((self.acceleration * distance + self.velocity**2 + vf**2) / 2)
        t_tot = (2 * v1 - self.velocity - vf) / self.acceleration

        # Update the velocity for the next segment
        self.velocity = vf
        return t_tot

    def calculate_turn_based_deceleration(self, p0, p1, p2):
        """
        Calculate deceleration factor based on the angle between the segments p0->p1 and p1->p2.
        """
        # Vector p0->p1
        v1 = (p1[0] - p0[0], p1[1] - p0[1])
        # Vector p1->p2
        v2 = (p2[0] - p1[0], p2[1] - p1[1])

        # Calculate the angle between v1 and v2 using the dot product
        dot_product = v1[0] * v2[0] + v1[1] * v2[1]
        mag_v1 = np.sqrt(v1[0]**2 + v1[1]**2)
        mag_v2 = np.sqrt(v2[0]**2 + v2[1]**2)

        cos_theta = dot_product / (mag_v1 * mag_v2)
        #angle = np.arccos(cos_theta)

        # Apply a penalty based on the sharpness of the turn
        deceleration_factor = np.clip(cos_theta, 0.5, 1.0)

        return deceleration_factor
