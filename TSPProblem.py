import random
import numpy as np
# read data from .tsp file, generate city information and
# distance matrix to calculate the cost and fitness function
class City:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

# read tsp file
def readFile(filepath):
    with open(filepath) as fp:  # read coordinate from file
        content = fp.read()
    start = content.index("NODE_COORD_SECTION") + 19
    lines = content[start:-5].split("\n")
    # print(lines)
    cities = []
    for line in lines:
        info = line.split(" ")
        city = City(int(info[0]), float(info[1]), float(info[2]))
        cities.append(city)
    length = cities.__len__()
    matrix = np.zeros((length + 1, length + 1))
    for city1 in cities:  # calculate the distance matrix
        for city2 in cities:
            distance = ((city1.x-city2.x)**2 + (city1.y-city2.y)**2)**0.5
            matrix[city1.num][city2.num] = distance
    return cities, matrix

# read opt.tour file to calculate the best permutation
def get_best(filepath, matrix):
    with open(filepath) as fp:  # read opt tour from file
        content = fp.read()
    start = content.index("TOUR_SECTION") + 13
    lines = content[start:-8].split("\n")
    cost = 0.0
    tick = 0
    for i in range(0, len(matrix)-2):
        tick += 1
        city1 = int(lines[i])
        city2 = int(lines[i + 1])
        cost += matrix[city1][city2]
    return cost

if __name__ == '__main__':
    path = "10datasets/tsp_file/eil51.tsp"
    cities, matrix = readFile(path)
    print(matrix[5][4])
