import pyrosim

# set sim to contain the simulator
sim = pyrosim.Simulator()


# pauses simulation at outset of program
sim = pyrosim.Simulator(play_paused=True, eval_time=1000)


# sends a cylinder into environment of length 1 radius 1
whiteObject = sim.send_cylinder(x=0, y=1, z=0.6, length=1.0, radius=0.1)
print(whiteObject)

redObject = sim.send_cylinder(x=0, y=1.5, z=1.1, length=1.0, radius=0.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)
print(whiteObject)

# starts simulation
sim.start()
