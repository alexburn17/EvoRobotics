import pyrosim
import matplotlib.pyplot as plt

# pauses simulation at outset of program
sim = pyrosim.Simulator(play_paused=True, eval_time=100)

# sends a cylinder into environment of length 1 radius 1
whiteObject = sim.send_cylinder(x=0, y=1, z=0.6, length=1.0, radius=0.1)

# sends a red cylinder into the environment
redObject = sim.send_cylinder(x=0, y=1.5, z=1.1, length=1.0, radius=0.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)

# creates a joint between the two cylinders
joint = sim.send_hinge_joint(first_body_id=whiteObject, second_body_id=redObject,
                             x=0, y=1, z=1.1,
                             n1=-1, n2=0, n3=0,
                             lo=-3.14159/2, hi=3.14159/2)

# add a sensor to the white cylinder
T0 = sim.send_touch_sensor(body_id=whiteObject)

# add a sensor to the red cylinder
T1 = sim.send_touch_sensor(body_id=redObject)

# adds a proprioceptive sensor to joint
P2 = sim.send_proprioceptive_sensor(joint_id=joint)

# adds a ray sensor to the end of the red cylinder:
#R3 = sim.send_ray_sensor(body_id=redObject, x=0, y=1.1, z=1.1, r1=0, r2=1, r3=0)
R3 = sim.send_ray_sensor(body_id=redObject, x=0, y=1.5, z=1, r1=0, r2=0, r3=-1)

# starts simulation
sim.start()

# tells your code to pause execution here until the simulation finishes running
sim.wait_to_finish()

# gets the sensor data
sensorData = sim.get_sensor_data(sensor_id=R3)

# prints the sensor data:
print(sensorData)

# creates a figure
f = plt.figure()

# adds the plotting space
panel = f.add_subplot(111)

# set plot limits (x and Y)
panel.set_ylim(-1, 11)

# plots the actual data:
plt.plot(sensorData)

# shows the plot:
plt.show()