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
# import statistics
Vertex = namedtuple('vertex', 'x y')
# This'll make the vertex tuple that we'll use for the chromosones.


# Example chromosone
# [vertex(1, 5), vertex(2, 6), vertex(8, 3), vertex(2, 1), vertex(8, 7),
#  vertex(3, 2)]


# class A(object):
#     def __init__(self):
#         pass


mutation_rate = 3  # (out of 100)

population_size = 256


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


class Individual():
    'Individuals for genetic algorithm. Has chromosone and related functions.'
    def __init__(self, input_chromosone=5):
        if input_chromosone == 5:
            self.chromosone = chromosonegen()
        else:
            self.chromosone = input_chromosone


def point_swap(chrom1, chrom2):
    """Swaps genes between two points in an input and output chromosone"""
    swap_pos = random.randint(0, 6)  # Randomly picks pos to swap at
    return chrom1[swap_pos:] + chrom2[:swap_pos]


def fragment_return(chromosone, startpos, endpos):
    return chromosone[startpos:endpos]


def evaluator(to_eval):
    x = to_eval.chromosone  # print (to_eval.chromosone)
    try:
        angle_set = [find_angle(x[5], x[0], x[1]),  # Run the find anglefunction
                     find_angle(x[0], x[1], x[2]),  # with all the vertcies
                     find_angle(x[1], x[2], x[3]),
                     find_angle(x[2], x[3], x[4]),
                     find_angle(x[3], x[4], x[5]),
                     find_angle(x[4], x[5], x[0])]
        total_error = 0
        for y in angle_set:
            total_error += math.fabs(60-y)  # Calculate totalerror withabs(60-y)
        # print (total_error)
        return total_error
    except ZeroDivisionError:
        return 360


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


def make_fitness_dict(population_list):
    fitness_dict = {}
    # print (population_dict)
    for x in population_list:
        fitness_dict[x] = round(evaluator(x))
    # inverse_fitness_dict = {}
    # for x in fitness_dict:
    #     inverse_fitness_dict[fitness_dict[x]] = x
    # return inverse_fitness_dict
    return fitness_dict


def invert_dict(dict_to_invert):
    inverted_dict = {}
    for x in dict_to_invert:
        inverted_dict[dict_to_invert[x]] = x
    return inverted_dict


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
    fitness_list = []
    for x in fitness_dict:
        fitness_list.append(fitness_dict[x])
    adjusted_fitness_list = []
    for x in sorted(fitness_list):  # step one & 2, sorting high-low
        adjusted_fitness_list.append(360-int(x))
    S = 0
    for x in adjusted_fitness_list:  # Step 3
        S += x
    r = random.randint(0, S)  # Step 4)
    adjusted_fitness_list = adjusted_fitness_list[::-1]
    s = 0  # Used for summing up values until greater than r
    x = 0  # Used for setting lastobj and summing up list stuff
    z = invert_dict(fitness_dict)
    lastobj = z[(adjusted_fitness_list[x]-360) * -1]
    x = 0
    while s < r:  # Step 5
        s += adjusted_fitness_list[x]  # Step 5 cont
        lastobj = z[(adjusted_fitness_list[x]-360) * -1]  # Lastobj
        x += 1
    winner = lastobj  # Step 6
    if evaluator(winner) == 360:
        winner = fitness_select(fitness_dict)
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
        # print (fitness_select(fitness_dict))
        x = fitness_select(fitness_dict).chromosone
        y = fitness_select(fitness_dict).chromosone
        while checker(x, y):
            y = fitness_select(fitness_dict).chromosone
            x = fitness_select(fitness_dict).chromosone
        return point_swap(x, y)


def checker(a, b):
    returns = False
    while n in a:
        for m in b:
            if n == m:
                returns = True
    return returns


def initiate_population():
    ''' Returns list of objects '''
    population_list = []
    for x in range(0, population_size):
        y = Individual()
        population_list.append(y)
    return population_list


def generate_generation(population_list):
    # takes fitness dictionary, makes list of new individuals, TODO
    for x in range(0, len(population_list)):
        population_list[x].chromosone = \
                        roulette_generate(make_fitness_dict(population_list), 1)
        # print ("generated generation " + str(x))
    return population_list


def mutation_chance(mutation_rate):
    x = random.randint(0, 100)
    if x < mutation_rate:
        return True
    else:
        return False


def random_mutation(individual):
    # x = random.randint(0, 128)
    # print (individual.chromosone)
    # chromosone_regen(individual)
    individual = chromosone_scramble(individual)
    # print (individual.chromosone)
    # if x < 8:
    #     individual = bound_mutation(individual)
    # elif x < 32:
    #     individual = chromosone_regen(individual)
    # elif x < 64:
    #     individual = chromosone_scramble(individual)
    # else:
    #     individual = arithmatic_mutation(individual)
    return individual


# def bound_mutation(individual):
#     if random.randint(0, 1) == 0:
#         # Lower Bound Mutation
#         y = Vertex(1, 1)
#         individual.chromosone = [y, y, y, y, y, y]
#     else:
#         # upper bound mutation
#         y = Vertex(10, 10)
#         individual.chromosone = [y, y, y, y, y, y]
#     return individual


# def arithmatic_mutation(individual):
#     x = random.randint(1, 4)
#     z = random.randint(1, 10)
#     a = random.randint(1, 10)
#     x = 1
#     temp = []
#     for y in range(len(temp)):
#         if x == 1:
#                 temp[y] = Vertex(individual.chromosone[y].x + z,
#                                  individual.chromosone[y].y + a)
#         elif x == 2:
#                 temp[y].x = individual.chromosone[y].x - z
#                 temp[y].y = individual.chromosone[y].y - a
#         elif x == 3:
#                 temp[y].x = individual.chromosone[y].x * z
#                 temp[y].y = individual.chromosone[y].z * a
#         elif x == 4:
#                 temp[y].x = individual.chromosone[y].x / z
#                 temp[y].y = individual.chromosone[y].z / a
#     return temp


def chromosone_regen(individual):
    individual.chromosone = chromosonegen
    return individual


def chromosone_scramble(individual):
    # for x in range(random.randint(0, 100)):
    individual.chromosone = \
        point_swap(individual.chromosone, individual.chromosone)
    return individual

popset = initiate_population()

# print(generate_generation(make_fitness_dict(popset)))
# for x in popset:
#     print (x)
x = make_fitness_dict(popset)
# print (x)
y = fitness_select(x)

# print (y.chromosone)
y = 0
for n in range(1024):
    x = make_fitness_dict(popset)
    popset = generate_generation(popset)
    y += 1
    print ("Generation " + str(y) + ". Example roulette selection is " +
           str(evaluator(fitness_select(x))))
    # for n in range(0, len(popset)):
    #     if mutation_chance(mutation_rate):
    #         popset[n] = random_mutation(popset[n])
    fitlist = []
    for z in x:
        fitlist.append(x[z])
    a = findmax(x, fitlist[0])
    print (a.chromosone)

