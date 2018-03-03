import pyrosim
from robot import ROBOT
import random

# for loop that creates n iterations
for i in range(0, 10):
    # starts simulation
    sim = pyrosim.Simulator(play_paused=False, eval_time=200)

    # call to function ROBOT which generates the scissor robot
    robot = ROBOT(sim, random.random()*2 - 1)

    # starts simulator
    sim.start()

    # tells your code to pause execution here until the simulation finishes running
    sim.wait_to_finish()




# gets the sensor data
#sensorData = sim.get_sensor_data(sensor_id=R3)

# prints the sensor data:
#print(sensorData)

# creates a figure
#f = plt.figure()

# adds the plotting space
#panel = f.add_subplot(111)

# set plot limits (x and Y)
#panel.set_ylim(-1, 11)

# plots the actual data:
#plt.plot(sensorData)

# shows the plot:
#plt.show()