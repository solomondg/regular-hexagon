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

Vertex = namedtuple('vertex', 'x y')  # This'll make the vertex tuple that we'll
                                      # use for the chromosones

# Example chromosone
# [vertex(1, 5), vertex(2, 6), vertex(8, 3), vertex(2, 1), vertex(8, 7),
#   vertex(3, 2)]


class Individual:
    'Individuals for genetic algorithm. Have chromosone and related functions.'
    def chromosonegen(self):
        """Make random chromosones, coord x, y | 0 < x < 10 """
        V1 = Vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        V2 = Vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        V3 = Vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        V4 = Vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        V5 = Vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        V6 = Vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        return [V1, V2, V3, V4, V5, V6]

    def __init__(self, chromosone=chromosonegen()):
        self.chromosone = chromosone
        self.mutation_rate = 0.02

    def point_swap(self, outside_chromosone, input_chromosone=chromosone):
        """Swaps genes between two points in an input and output chromosone"""
        swap_pos = random.randrange(1, 5, 1)
#       temp_chromosone1 = chromosone[:swap_pos]
#       temp_chromosone2 = outside_chromosone[swap_pos:]
        self.chromosone =\
        input_chromosone[:swap_pos] + outside_chromosone[swap_pos:]
