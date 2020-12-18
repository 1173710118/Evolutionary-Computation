from typing import Tuple
import solution as sl
import random
import numpy as np
import TSPProblem as tsp
import heapq

# different selection strategy
# fitness-proportional
def fitness(pool: [sl.Solution], matrix) -> [sl.Solution]:
    length = pool.__len__()
    print(length)
    points = []
    for elem in pool:
        points.append(elem.cal_cost(matrix) ** -1)
    points = points / min(points)
    sum_p = sum(points)

    candidate = []
    for i in range(0, int(0.5 * length)):
        choice = random.random() * sum_p
        for j in range(0, length):
            choice -= points[j]
            if choice <= 0:
                print("选择" + str(j))
                candidate.append(pool[j])
                break
    for i in candidate:
        print(i.cal_cost(matrix))
    return candidate

# elitism
def elitism(pool: [sl.Solution], matrix) -> [sl.Solution]:
    length = pool.__len__()
    # print(length)
    points = []
    # print(pool)
    for elem in pool:
        points.append(elem.cal_cost(matrix))
    # print(points)
    # print(heapq.nsmallest(int(0.5 * length), points))
    candidate = []
    for elem in heapq.nsmallest(int(0.5 * length), points):
        candidate.append(pool[points.index(elem)])
    # for i in candidate:
    #     print(i.cal_cost(matrix))
    return candidate

# tournament
def tournament(pool: [sl.Solution], matrix) -> [sl.Solution]:
    length = pool.__len__()
    # print(length)
    # print(heapq.nsmallest(int(0.5 * length), points))
    candidate = []
    for i in range(0, int(0.5 * length)):
        can1 = pool[2 * i]
        can2 = pool[2 * i + 1]
        if can1.cal_cost(matrix) >= can2.cal_cost(matrix):
            candidate.append(can2)
        else:
            candidate.append(can1)
    # for i in candidate:
    #     print(i.cal_cost(matrix))
    return candidate

if __name__ == '__main__':
    path = "10datasets/tsp_file/eil51.tsp"
    cities, matrix = tsp.readFile(path)
    size = cities.__len__()
    solution_pool = []
    for i in range(0, 10):
        solution = sl.Solution(size)
        solution_pool.append(solution)
    # fitness(solution_pool, matrix)
    tournament(solution_pool, matrix)
