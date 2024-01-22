import math
import numpy as np
from stl import mesh

def create_cog(radius, inner_radius, num_teeth, height, filename="cog.stl"):
    # Define some basic parameters
    tooth_depth = 0.1 * radius
    tooth_width = 2 * math.pi * radius / num_teeth

    # Create an empty mesh
    cog = mesh.Mesh(np.zeros(num_teeth * 12, dtype=mesh.Mesh.dtype))

    for i in range(num_teeth):
        angle = 2 * math.pi * i / num_teeth
        next_angle = 2 * math.pi * (i + 1) / num_teeth

        # Points for the tooth
        points = np.array([
            (radius * math.cos(angle), radius * math.sin(angle), 0),
            (radius * math.cos(next_angle), radius * math.sin(next_angle), 0),
            ((radius - tooth_depth) * math.cos(angle + tooth_width / 4), (radius - tooth_depth) * math.sin(angle + tooth_width / 4), 0),
            ((radius - tooth_depth) * math.cos(next_angle - tooth_width / 4), (radius - tooth_depth) * math.sin(next_angle - tooth_width / 4), 0),
            (inner_radius * math.cos(angle), inner_radius * math.sin(angle), 0),
            (inner_radius * math.cos(next_angle), inner_radius * math.sin(next_angle), 0),
            (radius * math.cos(angle), radius * math.sin(angle), height),
            (radius * math.cos(next_angle), radius * math.sin(next_angle), height),
            ((radius - tooth_depth) * math.cos(angle + tooth_width / 4), (radius - tooth_depth) * math.sin(angle + tooth_width / 4), height),
            ((radius - tooth_depth) * math.cos(next_angle - tooth_width / 4), (radius - tooth_depth) * math.sin(next_angle - tooth_width / 4), height),
            (inner_radius * math.cos(angle), inner_radius * math.sin(angle), height),
            (inner_radius * math.cos(next_angle), inner_radius * math.sin(next_angle), height),
        ])

        # Create the faces of the tooth
        faces = np.array([
            [0, 2, 4], [2, 5, 4], [2, 3, 5], [1, 3, 5],
            [6, 10, 8], [8, 10, 11], [8, 11, 9], [9, 11, 7],
            [0, 4, 6], [4, 10, 6], [1, 7, 5], [5, 7, 11],
            [2, 8, 3], [3, 8, 9]
        ])

        # Add the faces to the mesh
        cog.vectors[i * 12:(i + 1) * 12] = points[faces]

    # Write the mesh to file
    cog.save(filename)

# Example usage
create_cog(radius=10, inner_radius=5, num_teeth=20, height=5)

