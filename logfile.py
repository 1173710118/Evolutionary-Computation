from multiprocessing.pool import Pool
import TSPProblem as tsp
import solution as sl
import config
import crossover as co
import mutation as mt
import selection

population_size = 50
loop = 20000

# choose the best algorithm of PMX and insert and elitism
# with population size of 50, run 20000 loops
# record the best solution every 100 generations in different folder in 10datasets/log_file
def multi_processing(data_path):
    path = config.problem_path + data_path + ".tsp"
    cities, matrix = tsp.readFile(path)
    log_path = config.log_path + data_path + "/"

    for rep in range(0, 20):
        file = open(log_path + data_path + "_round" + str(rep + 1) + ".txt", "w")
        length = cities.__len__()
        population = []
        for i in range(0, population_size):
            solution = sl.Solution(length)
            population.append(solution)
        for i in range(0, loop):
            if i % 100 == 0:
                print(str(i) + "次")
                points = []
                for j in population:
                    points.append(j.cal_cost(matrix))
                print(round(min(points), 4))
                file.write(str(round(min(points), 4)) + " is the cost of " + data_path + "at " + str(i) + " run\n")
            co.Xover(population, method="pmx")  # crossover
            mt.mutate(population, method="insert")  # mutation
            population = selection.elitism(population, matrix)  # selection
        print(str(loop) + "次")
        for j in population:
            points.append(j.cal_cost(matrix))
        print(round(min(points), 4))
        file.write(str(round(min(points), 4)) + " is the cost of " + data_path + "at " + str(i) + " run\n")
        file.close()
if __name__ == "__main__":
    pool = Pool(processes=6)
    pool.map(multi_processing, config.datasets[7:8])
