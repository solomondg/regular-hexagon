# Genetic algorithm to generate 6 sided shapes. Fitness score is determined by
# regularity of angles. That is, it should generate a near perfect hexagon.

# Chromosones are a list of XY coordinates.
# More or less 6 genes, each with an XY pair defining the vertex.

# Simple roulette wheel selection.

# Fitness score in pseudocode. Lower is better.
# for genes in chromosone:
#   total_deviation += math.abs(gene_vertex.angle)

# There'll be 32 members of the population per generation.
# import sys
# import time
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


def varstore():
    varstore.mutation_rate = 0.02


class Individual():
    'Individuals for genetic algorithm. Has chromosone and related functions.'
    def chromosonegen():
        """Make random chromosones, coord x, y | 0 < x < 10 """
        vert1 = Vertex(round(random.random()*10, 3),
                       round(random.random()*10, 3))
        vert2 = Vertex(round(random.random()*10, 3),
                       round(random.random()*10, 3))
        vert3 = Vertex(round(random.random()*10, 3),
                       round(random.random()*10, 3))
        vert4 = Vertex(round(random.random()*10, 3),
                       round(random.random()*10, 3))
        vert5 = Vertex(round(random.random()*10, 3),
                       round(random.random()*10, 3))
        vert6 = Vertex(round(random.random()*10, 3),
                       round(random.random()*10, 3))
        return [vert1, vert2, vert3, vert4, vert5, vert6]

    def __init__(self, input_chromosone=chromosonegen()):
        self.chromosone = input_chromosone


def point_swap(input_chromosone, outside_chromosone):
    """Swaps genes between two points in an input and output chromosone"""
    swap_pos = random.randrange(1, 5, 1)  # Randomly picks pos to swap at
    return input_chromosone[:swap_pos] + outside_chromosone[swap_pos:]  # swaps


def fragment_return(chromosone, startpos, endpos):
    return chromosone[startpos:endpos]


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

# def roulette_gene_select(obj_set):# obj_set is 1d matrix/list with all objects
#     fitness_set = {}              # of current generation
#     for x in obj_set:
#         fitness_set[evaluator(x)] = x


def make_fitness_dict(object_list):
    fitness_dict = {}
    for x in object_list:
        fitness_dict[x] = evaluator(x)
    return fitness_dict


def fitness_select(fitness_dict):
    # How to roulette wheel select:
    # 1. Compute "inverse" fitness score (360 - fitness)
    # 2. Sort list from low to high fitness (maybe high to low, maybe random)
    # 3. find sum of all fitness scores, S
    # 4. Find random number r between 0 and S
    # 5. If fitness value of first object is smaller than r, add second object
    # fitness score. Repeat until greater than r
    # 6. Winner = last object whose fitness score was added (first to go over r)
    x = 0
    # print ("")
    adjusted_fitness_list = []
    for x in sorted(fitness_dict):  # step one & 2, sorting high-low
        adjusted_fitness_list.append(360-x)
    # print ('adjusted fitness list =', adjusted_fitness_list)
    S = 0
    for x in adjusted_fitness_list:  # Step 3
        S += x
    # print ('S = ', S)
    # r = random.random()*S
    r = random.randint(0, S)  # Step 4)
    # print ('r = ', r)
    adjusted_fitness_list = adjusted_fitness_list[::-1]
    s = 0  # Used for summing up values until greater than r
    x = 0  # Used for setting lastobj and summing up list stuff
    lastobj = fitness_dict[(adjusted_fitness_list[x]-360) * -1]
    x = 0
    while s < r:  # Step 5
        s += adjusted_fitness_list[x]  # Step 5 cont
        lastobj = fitness_dict[(adjusted_fitness_list[x]-360) * -1]  # Lastobj
        # print ('s =', s)
        # used for determining step6
        # print (type(x))
        x += 1
    # time.sleep(0.001)
    winner = lastobj  # Step 6
    return winner


def roulette_generate(fitness_dict, genmethod):
    '''generates chromosone from roulette wheel selection from a dictionary'''
    # genmethod is an int. Specifies how the new gene is generated
    # 0 = just copying
    # 1 = one-point selection (from two roulette winners)
    # 2 = one-point swap (from one roulette winner): TODO
    if genmethod == 0:
        return fitness_select(fitness_dict).chromosone
    elif genmethod == 1:
        return point_swap(fitness_select(fitness_dict).chromosone,
                          fitness_select(fitness_dict).chromosone)


def initiate_population():
    population_dict = {}
    for x in range(0, 128):
        population_dict[str('individual_'+str(x))] = Individual()
    return population_dict

popset = initiate_population()

# Just some tests
test_case = Individual()
