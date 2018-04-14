import pyrosim
import constants as c
from robotThree import ROBOT
import random
import math
import numpy



class INDIVIDUAL:
    def __init__(self, i):

        # Robot ID
        self.ID = i

        # genome is a vector of random numbers
        self.genome = numpy.random.random((7, 12)) * 2 - 1


        # fitness level (0 at outset)
        self.fitness = 0

    def Start_Evaluation(self, env, pp, pb):

        # starts simulation
        self.sim = pyrosim.Simulator(play_paused=pp, eval_time=c.evalTime, play_blind=pb)

        # call to function ROBOT which generates the bot
        self.robot = ROBOT(self.sim, self.genome)

        env.Send_To(self.sim)

        # starts simulator
        self.sim.start()

    def Compute_Fitness(self):

        # tells your code to pause execution here until the simulation finishes running
        self.sim.wait_to_finish()

        # get the sensor data from the position sensor (Y-axis)
        sensorData1 = self.sim.get_sensor_data(sensor_id=self.robot.L4, svi=0)

        # and print the data
        self.fitness = sensorData1[-1] + 0

        # deletes the copy of sim
        del self.sim

    def Mutate(self):
        # mutatates one of the genes based on a random number from 0 to three
        geneToMutatei = random.randint(0, 6)
        geneToMutatej = random.randint(0, 11)
        self.genome[geneToMutatei, geneToMutatej] = random.gauss(self.genome[geneToMutatei, geneToMutatej],
                                                                 math.fabs(self.genome[geneToMutatei, geneToMutatej]))

        if (self.genome[geneToMutatei, geneToMutatej] > 1):
            self.genome[geneToMutatei, geneToMutatej] = 1
        elif (self.genome[geneToMutatei, geneToMutatej] < -1):
            self.genome[geneToMutatei, geneToMutatej] = 1

    def Print(self):

        print('[', end='')

        print(self.ID, end='')

        print('  ', end='')

        print(self.fitness, end='')

        print(']', end='')











