from population import POPULATION
import constants as c
from environments import ENVIRONMENTS
import pickle
import csv
import os
import glob


finalData = []

for n in range(0, c.sampleSize):

    envs = ENVIRONMENTS()
    envs.Initialize()
    parents = POPULATION(c.popSize)
    parents.Initialize()
    parents.Evaluate(envs, pp=False, pb=True)
    parents.Print()

    data = []

    # for loop that creates n iterations
    for g in range(1, c.numGens):

       # create the child population
        children = POPULATION(c.popSize)
        # fill the children population from the parents keeping best in first place and
        # filling the rest with mutations
        children.Fill_From(parents)
        # evaluate the children
        children.Evaluate(envs, pp=False, pb=True)
        # print the fitness values
        print(g, end='  ')
        children.Print()
        #replace parents with stronger children
        parents.ReplaceWith(children)
        resultDat = children.Get_Data()
        data.append(resultDat)

        # save robot as new file name
        name = list("robot1.p")
        charN = str(n)
        name[5] = charN
        name = "".join(name)

        # save structure of child that fares well
        f = open(name, 'wb')
        pickle.dump(children, f)
        f.close()

    # append data set
    finalData.append(data)

# write out csv file
with open("Robot4_Rough.csv", "a") as fp:
    wr = csv.writer(fp, delimiter=',', quoting=csv.QUOTE_ALL)
    wr.writerow(finalData)

# get list of files in directory:
x = []
os.chdir('/Users/phillipburnham/EvoRobotics/BurnhamProject')
for file in glob.glob("*.p"):
    x.append(file)

# run those files
for j in range(0, len(x)):
    f = open(x[j], 'rb')
    best = pickle.load(f)
    f.close()
    best.Evaluate(envs, pp=True, pb=False)
