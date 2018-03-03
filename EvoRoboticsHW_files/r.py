from individual import INDIVIDUAL
import copy

# create instance of class INDIVIDUAL
parent = INDIVIDUAL()

# evaluate the individual
individual.Evaluate()

# print the fitness
print(individual.fitness)


# for loop that creates n iterations
for i in range(0, 1):

    child = copy.deepcopy(parent)

    print(parent.fitness, child.fitness)
