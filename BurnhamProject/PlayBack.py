from population import POPULATION
import constants as c
from environments import ENVIRONMENTS
import pickle
import csv
import os
import glob



#data = []

#for n in range(0, 30):

  #  envs = ENVIRONMENTS()
  #  envs.Initialize()
  #  parents = POPULATION(c.popSize)
  #  parents.Initialize()
  #  parents.Evaluate(envs, pp=False, pb=True, dt=0.05)
  #  parents.Print()

  #  resultDat = parents.Get_Data()
  #  data.append(resultDat)

# write out csv file
#with open("Robot4_Smooth_Random.csv", "a") as fp:
#    wr = csv.writer(fp, delimiter=',', quoting=csv.QUOTE_ALL)
#    wr.writerow(data)

envs = ENVIRONMENTS()
envs.Initialize()#

#envs = ENVIRONMENTS()
#envs.Initialize()
#arents = POPULATION(c.popSize)
#parents.Initialize()
#parents.Evaluate(envs, pp=True, pb=False, dt=0.05)
#parents.Print()



f = open("robot7.p", 'rb')
best = pickle.load(f)
f.close()
best.Evaluate(envs, pp=True, pb=False, dt=0.05)
best.Print()


# get list of files in directory:
#x = []
#os.chdir('/Users/phillipburnham/EvoRobotics/BurnhamProject/Robot3_Rough')
#for file in glob.glob("*.p"):
#    x.append(file)

#data = []
# run those files
#for j in range(0, len(x)):
#    f = open(x[j], 'rb')
#    best = pickle.load(f)
#    f.close()
#    best.Evaluate(envs, pp=False, pb=True, dt=0.05)
#    best.Print()

 #   resultDat = best.Get_Data()
 #   data.append(resultDat)

# write out csv file
#with open("Robot3_Rough_inSmooth.csv", "a") as fp:
#    wr = csv.writer(fp, delimiter=',', quoting=csv.QUOTE_ALL)
#    wr.writerow(data)
