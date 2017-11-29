import random
import string

alphabet = string.ascii_letters + " !'."

def get_answer():
    return "IQlCqnWXVoVDDRFKFevaFzxmUxTxONwlLSwfkxmG"

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

chrom_list = []
for i in range(0, 10):
    chrom_list.append(create_chromosome(len(get_answer())))

print("answer = {}".format(get_answer()))

print("generated list")
for chrom in chrom_list:
    print("{} = {}".format(chrom, get_score(chrom)))

print("selected list")
select_list = selection(chrom_list)
for chrom in select_list:
    print("{} = {}".format(chrom, get_score(chrom)))
