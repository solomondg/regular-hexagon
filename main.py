# Genetic algorithm to generate 6 sided shapes. Fitness score is determined by
# regularity of angles. That is, it should generate a near perfect hexagon.

# Chromosones are a list of XY coordinates.
# More or less 6 genes, each with an XY pair defining the vertex.

# Simple roulette wheel selection.

# Fitness score in pseudocode. Lower is better.
# for genes in chromosone:
#   total_deviation += math.abs(gene_vertex.angle)

# There'll be 32 members of the population per generation.

import random
import math
from collections import namedtuple

Vertex = namedtuple('vertex', 'x y')
# This'll make the vertex tuple that we'll use for the chromosones.


# Example chromosone
# [vertex(1, 5), vertex(2, 6), vertex(8, 3), vertex(2, 1), vertex(8, 7),
#  vertex(3, 2)]


# class A(object):
#     def __init__(self):
#         pass


class Individual():
    'Individuals for genetic algorithm. Has chromosone and related functions.'
    def chromosonegen():
        """Make random chromosones, coord x, y | 0 < x < 10 """
        vert1 = Vertex(random.random()*10,
                       random.random()*10)
        vert2 = Vertex(random.random()*10,
                       random.random()*10)
        vert3 = Vertex(random.random()*10,
                       random.random()*10)
        vert4 = Vertex(random.random()*10,
                       random.random()*10)
        vert5 = Vertex(random.random()*10,
                       random.random()*10)
        vert6 = Vertex(random.random()*10,
                       random.random()*10)
        return [vert1, vert2, vert3, vert4, vert5, vert6]

    def __init__(self, input_chromosone=chromosonegen()):
        self.chromosone = input_chromosone
        self.mutation_rate = 0.02


def point_swap(input_chromosone, outside_chromosone):
    """Swaps genes between two points in an input and output chromosone"""
    swap_pos = random.randrange(1, 5, 1)  # Randomly picks pos to swap at
    return input_chromosone[:swap_pos] + outside_chromosone[swap_pos:]  # swaps


def evaluator(to_eval):
    x = to_eval.chromosone
    angle_set = [find_angle(x[5], x[0], x[1]),  # Run the find angle function
                 find_angle(x[0], x[1], x[2]),  # with all the vertcies
                 find_angle(x[1], x[2], x[3]),
                 find_angle(x[2], x[3], x[4]),
                 find_angle(x[3], x[4], x[5]),
                 find_angle(x[4], x[5], x[0])]
    total_error = 0
    for y in angle_set:
        total_error += math.fabs(60-y)  # Calculate total error with abs(60-y)
    return total_error


def find_angle(vertA, vertB, vertC):
    # AB and BC is leg, CA is hypotenuse
    # Find distance of segments between that vertex and neightboring ones
    ab_dist = math.sqrt((vertB.x-vertA.x)**2 + (vertB.y - vertA.y)**2)
    bc_dist = math.sqrt((vertC.x-vertB.x)**2 + (vertC.y - vertB.y)**2)
    ca_dist = math.sqrt((vertA.x-vertC.x)**2 + (vertA.y - vertC.y)**2)
    # Calculate the angle (in radians)
    rad_angle = math.acos((ab_dist**2 + bc_dist**2 - ca_dist**2) /
                          (2*(ab_dist*bc_dist)))
    deg_angle = rad_angle * (180/math.pi)  # Change angle to degrees

    return deg_angle


# Just some tests
test_case = Individual()
print test_case.chromosone
print evaluator(test_case)
