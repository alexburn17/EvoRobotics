class ROBOT:
    def __init__(self, sim, wts):
        # sends a cylinder into environment of length 1 radius 1
        whiteObject = sim.send_cylinder(x=0, y=1, z=0.6, length=1.0, radius=0.1)

        # sends a red cylinder into the environment
        redObject = sim.send_cylinder(x=0, y=1.5, z=1.1, length=1.0, radius=0.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)

        # creates a joint between the two cylinders
        joint = sim.send_hinge_joint(first_body_id=whiteObject, second_body_id=redObject,
                                     x=0, y=1, z=1.1,
                                     n1=-1, n2=0, n3=0,
                                     lo=-3.14159 / 2, hi=3.14159 / 2)

        # add a sensor to the white cylinder
        T0 = sim.send_touch_sensor(body_id=whiteObject)

        # add a sensor to the red cylinder
        T1 = sim.send_touch_sensor(body_id=redObject)

        # adds a proprioceptive sensor to joint
        P2 = sim.send_proprioceptive_sensor(joint_id=joint)

        # adds a ray sensor to the end of the red cylinder:
        R3 = sim.send_ray_sensor(body_id=redObject, x=0, y=1.5, z=1, r1=0, r2=0, r3=-1)

        # send a sensor neuron to the sensor
        SN0 = sim.send_sensor_neuron(sensor_id=T0)

        # send a sensor neuron to the sensor
        SN1 = sim.send_sensor_neuron(sensor_id=T1)

        # send a sensor neuron to the sensor
        SN2 = sim.send_sensor_neuron(sensor_id=P2)

        # send a sensor neuron to the sensor
        SN3 = sim.send_sensor_neuron(sensor_id=R3)

        # create a dictionary called sensorNeurons to store sensor neurons
        sensorNeurons = {}

        # here we store each sensor neuron in a different index
        sensorNeurons[0] = SN0
        sensorNeurons[1] = SN1
        sensorNeurons[2] = SN2
        sensorNeurons[3] = SN3

        # add a motor neuron
        MN2 = sim.send_motor_neuron(joint_id=joint)

        # create a dictionary called motorNeurons to store sensor neurons
        motorNeurons = {}

        # here we store each sensor neuron in a different index
        motorNeurons[0] = MN2

        # for loop that creates synapses between each sensor neuron and the motor neuron MN2
        for s in sensorNeurons:
            for m in motorNeurons:
                sim.send_synapse(source_neuron_id=sensorNeurons[s], target_neuron_id=motorNeurons[m], weight=wts[s])


        # adds position sensor to robot
        self.P4 = sim.send_position_sensor(body_id=redObject)

