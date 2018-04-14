import constants as c
import random

class ROBOT:
    def __init__(self, sim, wts):

        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)

        del self.O
        del self.J
        del self.S
        del self.SN
        del self.MN

    def send_objects(self, sim):

        # send in an object
        self.O0 = sim.send_box(x=0, y=0, z=c.L + c.R, length=2.5*c.L, width=c.L, height=c.R * 2, r=.5, g=.5, b=.5)



        # sends a cylinder into environment
        self.O1 = sim.send_cylinder(x=c.L/1.4, y=c.L-c.R, z=c.L + c.R, length=c.L/2, radius=c.R, r=1, g=0, b=0, r1=1, r2=0, r3=0)

        # sends a cylinder into environment
        self.O2 = sim.send_cylinder(x=c.L/1.4, y=-c.L+c.R, z=c.L + c.R, length=c.L/2, radius=c.R, r=0, g=0, b=1, r1=1, r2=0, r3=0)

        # sends a cylinder into environment
        self.O3 = sim.send_cylinder(x=-c.L/1.4, y=c.L-c.R, z=c.L + c.R, length=c.L/2, radius=c.R, r=0, g=1, b=0, r1=1, r2=0, r3=0)

        # sends a cylinder into environment
        self.O4 = sim.send_cylinder(x=-c.L/1.4, y=-c.L+c.R, z=c.L + c.R, length=c.L/2, radius=c.R, r=1, g=0, b=1,  r1=1, r2=0, r3=0)

        # sends a cylinder into environment
        self.O5 = sim.send_cylinder(x=c.L, y=c.L-c.R, z=(c.L)/2 + c.R, length=c.L, radius=c.R, r=1, g=0, b=0, r1=0, r2=0, r3=1)

        # sends a cylinder into environment
        self.O6 = sim.send_cylinder(x=c.L, y=-c.L+c.R, z=(c.L)/2 + c.R, length=c.L, radius=c.R, r=0, g=0, b=1, r1=0, r2=0, r3=1)

        # sends a cylinder into environment
        self.O7 = sim.send_cylinder(x=-c.L, y=c.L-c.R, z=(c.L)/2 + c.R, length=c.L, radius=c.R, r=0, g=1, b=0, r1=0, r2=0, r3=1)

        # sends a cylinder into environment
        self.O8 = sim.send_cylinder(x=-c.L, y=-c.L+c.R, z=(c.L)/2 + c.R, length=c.L, radius=c.R, r=1, g=0, b=1, r1=0, r2=0, r3=1)



        # sends a cylinder into environment
        self.O9 = sim.send_cylinder(x=c.L/1.4, y=0, z=c.L + c.R, length=c.L / 2, radius=c.R, r=1, g=1, b=0,
                                    r1=1, r2=0, r3=0)

        # sends a cylinder into environment
        self.O10 = sim.send_cylinder(x=-c.L/1.4, y=0, z=c.L + c.R, length=c.L / 2, radius=c.R, r=0, g=0, b=0,
                                    r1=1, r2=0, r3=0)

        # sends a cylinder into environment
        self.O11 = sim.send_cylinder(x=-c.L, y=0, z=(c.L) / 2 + c.R, length=c.L, radius=c.R, r=0, g=0, b=0, r1=0,
                                    r2=0, r3=1)

        # sends a cylinder into environment
        self.O12 = sim.send_cylinder(x=c.L, y=0, z=(c.L) / 2 + c.R, length=c.L, radius=c.R, r=1, g=1, b=0,
                                    r1=0, r2=0, r3=1)




    def send_joints(self, sim):


        # creates a joint between the two cylinders
        self.J0 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O1,
                                       x=c.L/1.4, y=c.L-c.R, z=c.L+c.R,
                                       n1=-1, n2=0, n3=0)

        # creates a joint between the two cylinders
        self.J1 = sim.send_hinge_joint(first_body_id=self.O1, second_body_id=self.O5,
                                       x=c.L, y=c.L-c.R, z=c.L+c.R,
                                       n1=0, n2=-1, n3=0)

        # creates a joint between the two cylinders
        self.J2 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O2,
                                       x=c.L/1.4, y=-c.L+c.R, z=c.L+c.R,
                                       n1=-1, n2=0, n3=0)

        # creates a joint between the two cylinders
        self.J3 = sim.send_hinge_joint(first_body_id=self.O2, second_body_id=self.O6,
                                       x=c.L, y=-c.L+c.R, z=c.L+c.R,
                                       n1=0, n2=-1, n3=0)

        # creates a joint between the two cylinders THIS IS THE PROBLEM!
        self.J4 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O3,
                                       x=-c.L/1.4, y=c.L-c.R, z=c.L+c.R,
                                       n1=-1, n2=0, n3=0)

        # creates a joint between the two cylinders
        self.J5 = sim.send_hinge_joint(first_body_id=self.O3, second_body_id=self.O7,
                                       x=-c.L, y=c.L-c.R, z=c.L+c.R,
                                       n1=0, n2=-1, n3=0)

        # creates a joint between the two cylinders
        self.J6 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O4,
                                       x=-c.L/1.4, y=-c.L+c.R, z=c.L+c.R,
                                       n1=-1, n2=0, n3=0)

        # creates a joint between the two cylinders
        self.J7 = sim.send_hinge_joint(first_body_id=self.O4, second_body_id=self.O8,
                                       x=-c.L, y=-c.L+c.R, z=c.L+c.R,
                                       n1=0, n2=-1, n3=0)



        # creates a joint between the two cylinders
        self.J8 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O9,
                                       x=c.L/1.4, y=0, z=c.L+c.R,
                                       n1=-1, n2=0, n3=0)

        # creates a joint between the two cylinders
        self.J11 = sim.send_hinge_joint(first_body_id=self.O9, second_body_id=self.O12,
                                        x=c.L, y=0, z=c.L + c.R,
                                        n1=0, n2=-1, n3=0)


        # creates a joint between the two cylinders
        self.J10 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O10,
                                       x=-c.L/1.4, y=0, z=c.L+c.R,
                                       n1=-1, n2=0, n3=0)


        # creates a joint between the two cylinders
        self.J9 = sim.send_hinge_joint(first_body_id=self.O10, second_body_id=self.O11,
                                       x=-c.L, y=0, z=c.L+c.R,
                                       n1=0, n2=-1, n3=0)





    def send_sensors(self, sim):

        # add a sensor to the white cylinder
        self.T0 = sim.send_touch_sensor(body_id=self.O5)

        # add a sensor to the red cylinder
        self.T1 = sim.send_touch_sensor(body_id=self.O6)

        # adds a proprioceptive sensor to joint
        self.T2 = sim.send_touch_sensor(body_id=self.O7)

        # adds a ray sensor to the end of the red cylinder:
        self.T3 = sim.send_touch_sensor(body_id=self.O8)

        # adds a proprioceptive sensor to joint
        self.T4 = sim.send_touch_sensor(body_id=self.O11)

        # adds a ray sensor to the end of the red cylinder:
        self.T5 = sim.send_touch_sensor(body_id=self.O12)

        # adds position sensor to robot
        self.L4 = sim.send_light_sensor(body_id=self.O0)

    def send_neurons(self, sim):

        self.O = {}
        self.O[0] = self.O0
        self.O[1] = self.O1
        self.O[2] = self.O2
        self.O[3] = self.O3
        self.O[4] = self.O4
        self.O[5] = self.O5
        self.O[6] = self.O6
        self.O[7] = self.O7
        self.O[8] = self.O8
        self.O[9] = self.O9
        self.O[10] = self.O10
        self.O[11] = self.O11
        self.O[12] = self.O12



        self.J = {}
        self.J[0] = self.J0
        self.J[1] = self.J1
        self.J[2] = self.J2
        self.J[3] = self.J3
        self.J[4] = self.J4
        self.J[5] = self.J5
        self.J[6] = self.J6
        self.J[7] = self.J7
        self.J[8] = self.J8
        self.J[9] = self.J9
        self.J[10] = self.J10
        self.J[11] = self.J11


        self.S = {}
        self.S[0] = self.T0
        self.S[1] = self.T1
        self.S[2] = self.T2
        self.S[3] = self.T3
        self.S[4] = self.T4
        self.S[5] = self.T5
        self.S[6] = self.L4

        self.SN = {}
        self.MN = {}

        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id=self.S[s])

        for j in self.J:
            self.MN[j] = sim.send_motor_neuron(joint_id=self.J[j], tau=1)


    def send_synapses(self, sim, wts):

        for j in self.SN:
            for i in self.MN:
                sim.send_synapse(source_neuron_id=self.SN[j], target_neuron_id=self.MN[i], weight=wts[j, i])

        # for loop that creates synapses between each sensor neuron and the motor neuron MN2
        #for s in self.sensorNeurons:
         #   for m in self.motorNeurons:
          #      sim.send_synapse(source_neuron_id=self.sensorNeurons[s], target_neuron_id=self.motorNeurons[m], weight=wts[s])


