from individual import INDIVIDUAL

import pickle

f = open('robot1.p', 'rb')

best = pickle.load(f)
f.close()

best.Evaluate()

