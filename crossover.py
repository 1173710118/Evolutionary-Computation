from typing import Tuple
import solution as sl
import random
import numpy as np


# order crossover
def order(p1: sl.Solution, p2: sl.Solution) -> Tuple[sl.Solution, sl.Solution]:
    length = p1.length
    pm1 = p1.permutation
    pm2 = p2.permutation
    off_spring1 = sl.Solution(length)
    off_spring2 = sl.Solution(length)
    lis = range(0, length)
    temp = random.sample(lis, 2)
    position1 = min(temp[0], temp[1])
    position2 = max(temp[0], temp[1])
    # print(position1)
    # print(position2)
    substring1 = pm1[position1:position2]
    substring2 = pm2[position1:position2]
    # print(substring1)
    # print(substring2)
    set1 = {-1}
    set2 = {-1}
    for i in substring1:
        set1.add(i)
    for i in substring2:
        set2.add(i)
    set1.remove(-1)
    set2.remove(-1)
    # print(set1)
    # print(set2)
    off_spring1.permutation[position1:position2] = substring1
    off_spring2.permutation[position1:position2] = substring2
    point1 = position2
    point2 = position2
    for i in range(position2, length):
        if not set1.__contains__(pm2[i]):
            off_spring1.permutation[point1] = pm2[i]
            point1 += 1
        if not set2.__contains__(pm1[i]):
            off_spring2.permutation[point2] = pm1[i]
            point2 += 1
    for i in range(0, position2):
        if point1 == length:
            point1 = 0
        if point2 == length:
            point2 = 0
        if not set1.__contains__(pm2[i]):
            off_spring1.permutation[point1] = pm2[i]
            point1 += 1
        if not set2.__contains__(pm1[i]):
            off_spring2.permutation[point2] = pm1[i]
            point2 += 1
    return off_spring1, off_spring2


# pmx crossover
def pmx(p1: sl.Solution, p2: sl.Solution) -> Tuple[sl.Solution, sl.Solution]:
    length = p1.length
    pm1 = p1.permutation
    pm2 = p2.permutation
    osp1 = []
    osp2 = []
    for i in range(0, length):
        osp1.append(0)
        osp2.append(0)
    lis = range(0, length)
    temp = random.sample(lis, 2)
    position1 = min(temp[0], temp[1])
    position2 = max(temp[0], temp[1])
    # print(position1)
    # print(position2)
    substring1 = pm1[position1:position2]
    substring2 = pm2[position1:position2]
    set1 = {-1}
    set2 = {-1}
    for i in substring1:
        set1.add(i)
    for i in substring2:
        set2.add(i)
    set1.remove(-1)
    set2.remove(-1)
    osp1[position1:position2] = substring1
    osp2[position1:position2] = substring2
    for i in range(position1, position2):
        if not set1.__contains__(pm2[i]):
            allele = pm2[i]
            position = i
            while True:
                if osp1[position] == 0:
                    osp1[position] = allele
                    break
                anallele = pm1[position]
                position = pm2.index(anallele)

        if not set2.__contains__(pm1[i]):
            allele = pm1[i]
            position = i
            while True:
                if osp2[position] == 0:
                    osp2[position] = allele
                    break
                anallele = pm2[position]
                position = pm1.index(anallele)
    for i in range(0, length):
        if osp1[i] == 0:
            osp1[i] = pm2[i]
        if osp2[i] == 0:
            osp2[i] = pm1[i]
    off_spring1 = sl.Solution(length)
    off_spring2 = sl.Solution(length)
    off_spring1.permutation = osp1
    off_spring2.permutation = osp2
    # print(type(osp1[0]))
    # print(osp2)
    return off_spring1, off_spring2


# cycle crossover
def cycle(p1: sl.Solution, p2: sl.Solution) -> Tuple[sl.Solution, sl.Solution]:
    length = p1.length
    pm1 = p1.permutation.copy()
    pm2 = p2.permutation.copy()
    cycles = []
    start = 0

    while True:
        for i in range(0, length):
            if pm1[i] != 0:
                start = i
                break
        if pm1[start] == 0:
            break
        cycle = []
        position = start
        while True:
            allele = pm2[position]
            position = pm1.index(allele)
            cycle.append(position)
            if position == start:
                break
        for i in cycle:
            pm1[i] = 0
        cycles.append(cycle)
    # print(cycles)
    osp1 = []
    osp2 = []
    for i in range(0, length):
        osp1.append(0)
        osp2.append(0)
    for i in range(0, cycles.__len__()):
        for elem in cycles[i]:
            if i % 2 == 0:
                osp1[elem] = p1.permutation[elem]
                osp2[elem] = p2.permutation[elem]
            else:
                osp2[elem] = p1.permutation[elem]
                osp1[elem] = p2.permutation[elem]
    off_spring1 = sl.Solution(length)
    off_spring2 = sl.Solution(length)
    off_spring1.permutation = osp1
    off_spring2.permutation = osp2
    return off_spring1, off_spring2


# edge recombination crossover
def edge_recombination(p1: sl.Solution, p2: sl.Solution) -> sl.Solution:
    length = p1.length
    pm1 = p1.permutation.copy()
    pm2 = p2.permutation.copy()
    table = []
    for i in range(0, length):
        entry = [pm1[i]]
        edges = [pm1[i - 1]]
        if i + 1 == length:
            edges.append(pm1[0])
        else:
            edges.append(pm1[i + 1])
        entry.append(edges)
        table.append(entry)

    for i in range(0, length):
        edges = [pm2[i - 1]]
        if i + 1 == length:
            edges.append(pm2[0])
        else:
            edges.append(pm2[i + 1])
        for j in table:
            if j[0] == pm2[i]:
                j[1].extend(edges)
                break
    print(table)
    osp = []
    allele = random.randint(1, length + 1)
    while osp.__len__() != length:
        osp.append(allele)
        for j in table:
            if j[1].__contains__(allele):
                j[1].remove(allele)
            if j[1].__contains__(allele):
                j[1].remove(allele)
        print(allele)
        print(table)
        choices = []
        for j in range(0, table.__len__()):
            if table[j][0] == allele:
                choices = table[j][1]
                table[j] = 0
                table.remove(0)
                break
        print(choices)
        for i in choices:
            if choices.count(i) == 2:
                allele = i
                break

        for i in choices:
            lengths = []
            for j in range(0, table.__len__()):
                if table[j][0] == i:
                    lengths.append(table[j][1].__len__())
                    break
        if max(lengths) == min(lengths):
            if choices.__len__() > 0:
                allele = choices[random.randint(0, choices.__len__() - 1)]
        else:
            allele = choices[choices.index(min(length))]
    print(osp)
    off_spring = sl.Solution(length)
    off_spring.permutation = osp
    return off_spring


# choose different crossover method
def Xover(population: [sl.Solution], method="order"):
    size = population.__len__()
    offsprings = []
    for i in range(0, int(size / 2)):
        if method == "order":
            offsprings.extend(order(population[i * 2], population[i * 2 + 1]))
        elif method == "pmx":
            offsprings.extend(pmx(population[i * 2], population[i * 2 + 1]))
        elif method == "cycle":
            offsprings.extend(cycle(population[i * 2], population[i * 2 + 1]))
        elif method == "edge":
            offsprings.append(edge_recombination(population[i * 2], population[i * 2 + 1]))
    population.extend(offsprings)


if __name__ == '__main__':
    solution1 = sl.Solution(9)
    solution2 = sl.Solution(9)
    # print(solution1.permutation)
    # print(solution2.permutation)
    # solution1.permutation = [1,2,3,4,5,6,7,8,9]
    # solution2.permutation = [9,3,7,8,2,6,5,1,4]
    # os1, os2 = order(solution1, solution2)
    # os1, os2 = cycle(solution1, solution2)
    # edge_recombination(solution1,solution2)
    # print(os1.permutation)
    # print(os2.permutation)
