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
import math
from collections import namedtuple

vertex = namedtuple('vertex', 'x y')

# Example chromosone
# [vertex(1, 5), vertex(2, 6), vertex(8, 3), vertex(2, 1), vertex(8, 7),
#   vertex(3, 2)]


class individual:
    'Individuals for genetic algorithm. Have chromosone and related functions.'
    def chromosonegen():
        v1 = vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        v2 = vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        v3 = vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        v4 = vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        v5 = vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        v6 = vertex(random.randrange(0, 10, 1), random.randrange(0, 10, 1))
        return [v1, v2, v3, v4, v5, v6]

    def __init__(self, chromosone=chromosonegen):
        self.chromosone = chromosone
        mutation_rate = 0.02

    def point_swap(self, chromosone=self.chromosone, outside_chromosone):
#        swap_pos = random.randrange(1, 5, 1)
#         temp_chromosone1 = chromosone[:swap_pos]
#        temp_chromosone2 = outside_chromosone[swap_pos:]
#        self.chromosone = test_chromosone1 + test_chromosone2

