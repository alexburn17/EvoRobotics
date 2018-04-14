from individual import INDIVIDUAL
import copy
import numpy
import constants as c

class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize

    def Print(self):
        print('\n')
        for i in self.p:
            if i in self.p:
                self.p[i].Print()

    def Get_Data(self):
        result = []
        for i in self.p:
            result.append(self.p[i].fitness)
            return result[-1]

    def Evaluate(self, envs, pp, pb):
        for i in self.p:
            self.p[i].Fitness = 0
        for e in range(0, c.numEnvs):
            for i in self.p:
                self.p[i].Start_Evaluation(envs.envs[e], pp, pb)
            for i in self.p:
                self.p[i].Compute_Fitness()
        #for z in self.p:
         #   self.p[z].fitness = self.p[z].fitness


    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def Initialize(self):
        for i in range(0, self.popSize):
            self.p[i] = INDIVIDUAL(i)

    def Copy_Best_From(self, other):

        c = [0] * len(other.p)
        for i in other.p:
            c[i] = copy.deepcopy(other.p[i].fitness)
        self.p[0] = other.p[c.index(max(c))]


    def Fill_From(self, other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)

    def Collect_Children_From(self, other):
        for j in range(1, self.popSize):
            winner = self.Winner_Of_Tournament_Selection(other)
            self.p[j] = copy.deepcopy(other.p[winner])
            self.p[j].Mutate()

    def Winner_Of_Tournament_Selection(self, other):

        p1 = numpy.random.choice(other.popSize)
        p2 = numpy.random.choice(other.popSize)

        while p1 == p2:
            p2 = numpy.random.choice(other.popSize)


        if other.p[p1].fitness > other.p[p2].fitness:
            return p1
        else:
            return p2

        #p1 = random.randint(1, len(other.p) - 1)
        #p2 = random.randint(1, len(other.p) - 1)
        #while p2 == p1:
        #    p2 = random.randint(1, len(other.p) - 1)
        #if other.p[p1].fitness > other.p[p2].fitness:
        #    return other.p[p1]
        #elif other.p[p1].fitness < other.p[p2].fitness:
        #    return other.p[p2]

    def ReplaceWith(self, other):
        for i in self.p:
            if self.p[i].fitness < other.p[i].fitness:
                self.p[i] = other.p[i]

















