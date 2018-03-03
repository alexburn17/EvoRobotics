from population import POPULATION
import copy
import pickle


parents = POPULATION(10)
parents.Evaluate(pb=True)
#exit()
parents.Print()


# for loop that creates n iterations
for g in range(1, 200):

    # makes a copy of parents
    children = copy.deepcopy(parents)

    # mutates the parents to make the children
    children.Mutate()

    # evaluates the children
    children.Evaluate(pb=True)

    # if they do better, they replace the parents
    parents.ReplaceWith(children)

    # print generation
    print(g, end='')

    # print the fitness
    parents.Print()

    # save structure of child that fares well
    f = open('robot1.p', 'wb')
    pickle.dump(parents, f)
    f.close()

f = open('robot1.p', 'rb')

best = pickle.load(f)
f.close()

best.Evaluate(pb=False)












