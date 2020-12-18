import solution as sl
import random


#  insert operator
def insert(solution: sl.Solution):
    permutation = solution.permutation
    lis = range(0, permutation.__len__())
    # print(lis.__len__())
    temp = random.sample(lis, 2)
    position1 = min(temp[0], temp[1])
    position2 = max(temp[0], temp[1])
    temp_allele = permutation[position2]
    # print(position1)
    # print(position2)
    for i in range(0, position2 - position1 - 1):
        permutation[position2 - i] = permutation[position2 - i - 1]
    permutation[position1 + 1] = temp_allele
    solution.permutation = permutation
    return permutation


#  swap operator
def swap(solution: sl.Solution):
    permutation = solution.permutation
    lis = range(0, permutation.__len__())
    temp = random.sample(lis, 2)
    position1 = min(temp[0], temp[1])
    position2 = max(temp[0], temp[1])
    temp_allele = permutation[position2]
    permutation[position2] = permutation[position1]
    permutation[position1] = temp_allele
    solution.permutation = permutation
    return permutation


#  inversion operator
def inversion(solution: sl.Solution):
    permutation = solution.permutation
    lis = range(0, permutation.__len__())
    temp = random.sample(lis, 2)
    position1 = min(temp[0], temp[1])
    position2 = max(temp[0], temp[1])
    # print(position2)
    substring = permutation[position1:position2]
    # print(substring)
    for i in range(0, substring.__len__()):
        permutation[i + position1] = substring[-(i + 1)]
    solution.permutation = permutation
    return permutation


#  scramble operator
def scramble(solution: sl.Solution):
    permutation = solution.permutation
    lis = range(0, permutation.__len__())
    temp = random.sample(lis, 2)
    position1 = min(temp[0], temp[1])
    position2 = max(temp[0], temp[1])
    # print(position1)
    # print(position2)
    substring = permutation[position1:position2]
    # print(substring)
    random.shuffle(substring)
    for i in range(0, substring.__len__()):
        permutation[i + position1] = substring[-(i + 1)]
    solution.permutation = permutation
    return permutation


# choose different mutation operator
def mutate(population: [sl.Solution], method="insert"):
    size = len(population)
    for i in range(int(0.5 * size), size):
        if method == "insert":
            insert(population[i])
        elif method == "swap":
            swap(population[i])
        elif method == "inversion":
            inversion(population[i])
        elif method == "scramble":
            scramble(population[i])

if __name__ == '__main__':
    solution = sl.Solution(10)
    print(solution.permutation)
    # insert(solution)
    # swap(solution)
    # inversion(solution)
    # scramble(solution)
    print(solution.permutation)
