from population import POPULATION
import constants as c
from environments import ENVIRONMENTS
import pickle

envs = ENVIRONMENTS()
envs.Initialize()
parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp=True, pb=False)
#parents.Print()


# create parent pop of popSize
#parents = POPULATION(c.popSize)
# initialize pop size for parents
#parents.Initialize()
# evaluate by running sim and calculating fitness
#parents.Evaluate(envs, pp=False, pb=True)
# print fitness values
#parents.Print()


# for loop that creates n iterations
#for g in range(1, c.numGens):

    # create the child population
  #  children = POPULATION(c.popSize)
    # fill the children popualtion from the parents keeping best in first place and
    # filling the rest with mutations
  #  children.Fill_From(parents)
    # evaluate the children
  #  children.Evaluate(envs, pp=False, pb=True)
    # print the fitness values
  #  print(g, end='  ')
  #  children.Print()
    #replace parents with stronger children
#    parents.ReplaceWith(children)



# save structure of child that fares well
  #  f = open('robot1.p', 'wb')
  #  pickle.dump(children, f)
  #  f.close()




#f = open('robot1.p', 'rb')

#best = pickle.load(f)
#f.close()

#best.Evaluate(envs, pp=False, pb=False)












