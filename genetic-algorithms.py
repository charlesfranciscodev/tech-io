import random
import string
import sys

alphabet = string.ascii_letters + " !'."

def get_answer():
    return "IQlCqnWXVoVDDRFKFevaFzxmUxTxONwlLSwfkxmG"

def is_answer(chrom):
    return chrom == get_answer()

def get_mean_score(population):
    total_score = 0
    for chrom in population:
        total_score += get_score(chrom)
    return total_score

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    chrom = ""
    for i in range(0, size):
        chrom += get_letter()
    return chrom

# compare the chromosome with the solution (how many character are in the correct position?)
# floating number between 0 and 1. The better the chromosome, the closer to 1
def get_score(chrom):
    key = get_answer()
    i = 0
    correct = 0
    while i < len(key) and i < len(chrom):
        if  key[i] == chrom[i]:
            correct += 1
        i += 1
    return correct / len(key)
    
def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
    # Sort individuals by their fitting score
    chromosomes_list.sort(key=lambda chrom: get_score(chrom))
    # Select the best individuals
    index = int(len(chromosomes_list) * (1 - GRADED_RETAIN_PERCENT))
    nb_remaining_to_pick = int(len(chromosomes_list) * NONGRADED_RETAIN_PERCENT)
    selected = chromosomes_list[index:]
    # Remove already selected individuals
    remaining_list = chromosomes_list[:index]
    # Randomly select other individuals
    for _ in range(0, nb_remaining_to_pick):
        selected.append(random.choice(remaining_list))
    return selected

def crossover(parent1, parent2):
    #  * Select half of the parent genetic material
    slice_index1 = int(len(parent1) / 2)
    slice_index2 = int(len(parent2) / 2)
    half_parent1 = parent1[:slice_index1]
    half_parent2 = parent2[slice_index2:]
    child = half_parent1 + half_parent2
    #  * Return the new chromosome
    #  * Genes should not be moved
    return child

def mutation(chrom):
    #  * Random gene mutation : a character is replaced
    random_index = random.randint(0, len(chrom) - 1)
    mutated_chrom = chrom[:random_index] + get_letter() + chrom[random_index + 1:]
    return mutated_chrom

# Algorithm
def create_population(pop_size, chrom_size):
    population = []
    for i in range(0, pop_size):
        chrom = create_chromosome(chrom_size)
        population.append(chrom)
    return population
    
def generation(population):
    select = selection(population)
    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    nb_children = len(population) - len(select)

    while len(children) < nb_children:
        ## crossover
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        child = crossover(parent1, parent2)
        ## mutation
        # use the mutation(child) function created on exercise 2
        child = mutation(child)
        children.append(child)
    
    # return the new generation
    return select + children

def algorithm():
    chrom_size = int(input())
    population_size = 10
    # create the base population
    population = create_population(population_size, chrom_size)
    answers = []
    
    # while a solution has not been found
    while not answers:
        # create the next generation
        population = generation(population)
        # display the average score of the population (watch it improve)
        # print(get_mean_score(population), file=sys.stderr)
        # check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)
    
    # print the solution
    print(answers[0])

algorithm()
