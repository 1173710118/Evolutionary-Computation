import random
import numpy as np
import TSPProblem

# represent a possible solution to the problem
# initialize with a random permutation
class Solution:
    def __init__(self, length):
        self.length = length
        permutation = []
        for i in range(0, length):
            permutation.append(i + 1)
        random.shuffle(permutation)
        self.permutation = permutation

    def cal_cost(self, matrix):
        permutation = self.permutation
        cost = 0.0
        for i in range(0, self.length - 1):
            city1 = permutation[i]
            city2 = permutation[i+1]
            try:
                cost += matrix[city1][city2]
            except IndexError:
                print(city1)
                print(city2)
                exit(0)
        return cost


if __name__ == '__main__':
    print()
