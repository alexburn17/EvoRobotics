from individual import INDIVIDUAL
import copy
import pickle

# creates class indivual called parent
parent = INDIVIDUAL()

# evaluates the parent
parent.Evaluate(False)


# for loop that creates n iterations
for i in range(0, 20):

    # makes a copy of parent
    child = copy.deepcopy(parent)

    # mutates the child genoame
    child.Mutate()

    # evaluates the child
    child.Evaluate(True)

    # prints both fitness values
    print('[g:', i, ']','[pw:', parent.genome, ']', '[p:', parent.fitness, ']', '[c:', child.fitness, ']')

    # if the child has higher fitness then the parent, become the child
    if (child.fitness > parent.fitness):
        parent = child

        # if does better then parent show image
        parent.Evaluate(False)

        # save structure of child that fares well
        f = open('robot.p', 'wb')
        pickle.dump(parent, f)
        f.close()



