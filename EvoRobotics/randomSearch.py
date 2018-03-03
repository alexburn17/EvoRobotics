import pyrosim
from individual import INDIVIDUAL


# for loop that creates n iterations
for i in range(0, 10):

    individual = INDIVIDUAL()

    individual.Evaluate()

    print(individual.fitness)


    # starts simulation
    #sim = pyrosim.Simulator(play_paused=False, eval_time=200)

    # call to function ROBOT which generates the scissor robot
    #robot = ROBOT(sim, random.random()*2 - 1)

    # starts simulator
    #sim.start()

    # tells your code to pause execution here until the simulation finishes running
    #sim.wait_to_finish()

    # get the sensor data from the position sensor (X-axis)
    #sensorData0 = sim.get_sensor_data(sensor_id=robot.P4, svi = 0)

    # get the sensor data from the position sensor (Y-axis)
    #sensorData1 = sim.get_sensor_data(sensor_id=robot.P4, svi = 1)

    # get the sensor data from the position sensor (Z-axis)
    #sensorData2 = sim.get_sensor_data(sensor_id=robot.P4, svi = 2)

    # and print the data
    #print(sensorData1[-1])



