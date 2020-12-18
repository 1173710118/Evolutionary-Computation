import TSPProblem as tsp
import solution as sl
import config
import crossover as co
import mutation as mt
import selection
# adjust different parameters of population size and number of generations
population_size = 50
loop = 20000

if __name__ == "__main__":
    path = "10datasets/tsp_file/pcb442.tsp"  # choose different problem
    cities, matrix = tsp.readFile(path)
    length = cities.__len__()

    population = []
    for i in range(0, population_size):
        solution = sl.Solution(length)
        population.append(solution)
    for i in range(0, loop):
        if i % 5000 == 0 and i != 15000:
            print(str(i) + "次")
            points = []
            for j in population:
                points.append(j.cal_cost(matrix))
            print(round(min(points), 4))
        co.Xover(population, method="pmx")  # crossover
        mt.mutate(population, method="insert")  # mutation
        population = selection.elitism(population, matrix)  # selection
    print(str(loop) + "次")
    for j in population:
        points.append(j.cal_cost(matrix))
    print(round(min(points), 4))
