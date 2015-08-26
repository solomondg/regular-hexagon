# Genetic algorithm to generate 6 sided shapes. Fitness score is determined by
# regularity of angles. That is, it should generate a near perfect hexagon.j

# Chromosones are a list of XY coordinates.
# More or less 6 genes, each with an XY pair defining the vertex.

# Simple roulette wheel selection.

# Fitness score in pseudocode. Lower is better.
# for genes in chromosone:
#   total_deviation += math.abs(gene_vertex.angle)

# For the sake of theme, there'll be 6 members of the population per generation.

import random
# import math
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
        vert1 = Vertex(random.randrange(0, 10, 1),
                       random.randrange(0, 10, 1))
        vert2 = Vertex(random.randrange(0, 10, 1),
                       random.randrange(0, 10, 1))
        vert3 = Vertex(random.randrange(0, 10, 1),
                       random.randrange(0, 10, 1))
        vert4 = Vertex(random.randrange(0, 10, 1),
                       random.randrange(0, 10, 1))
        vert5 = Vertex(random.randrange(0, 10, 1),
                       random.randrange(0, 10, 1))
        vert6 = Vertex(random.randrange(0, 10, 1),
                       random.randrange(0, 10, 1))
        return [vert1, vert2, vert3, vert4, vert5, vert6]

    def __init__(self, input_chromosone=chromosonegen()):
        self.chromosone = input_chromosone
        self.mutation_rate = 0.02

    @classmethod
    def point_swap(self, input_chromosone, outside_chromosone):
        """Swaps genes between two points in an input and output chromosone"""
        swap_pos = random.randrange(1, 5, 1)
#       temp_chromosone1 = chromosone[:swap_pos]
#       temp_chromosone2 = outside_chromosone[swap_pos:]
        self.chromosone =\
            input_chromosone[:swap_pos] + outside_chromosone[swap_pos:]

test_case = Individual()
print test_case.chromosone
print test_case.mutation_rate
