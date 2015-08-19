# Genetic algorithm to generate 6 sided shapes. Fitness score is determined by
# regularity of angles. That is, it should generate a near perfect hexagon.

# Chromosones take the form of g1[x, y]g2[x, y]g3[x, y]g4[x, y]g5[x, y]g6[x, y];
# more or less 6 genes, each with an XY pair.

# Simple roulette wheel selection.

# Fitness score in pseudocode
# for genes in chromosone:
#   total_deviation += math.abs(gene_vertex.angle)

# For the sake of theme, there'll be 6 members of the population per generation.

import random
import math



