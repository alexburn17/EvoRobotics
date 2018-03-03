from population import POPULATION
import copy
import pickle


parents = POPULATION(10)
parents.Initialize()
parents.Evaluate(pb=True)
parents.Print()


# for loop that creates n iterations
for g in range(1, 200):

    children = POPULATION(10)

    children.Fill_From(parents)

    children.Evaluate(pb=True)

    print(g, end='  ')
    children.Print()

    parents.ReplaceWith(children)



# save structure of child that fares well
    f = open('robot1.p', 'wb')
    pickle.dump(children, f)
    f.close()




f = open('robot1.p', 'rb')

best = pickle.load(f)
f.close()

best.Evaluate(pb=False)












