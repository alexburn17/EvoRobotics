import constants as c



class ENVIRONMENT:
    def __init__(self, e):
        # Environment ID
        self.ID = e

        self.l = c.L
        self.w = c.L
        self.h = c.L

        if self.ID == 0:
            self.Place_Light_Source_To_The_Front()


    def Place_Light_Source_To_The_Front(self):

        self.x = c.L * 0
        self.y = c.L * c.dist
        self.z = c.L * 0


    def Send_To(self, sim):
        lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h)
        sim.send_light_source(body_id=lightSource)

        for l in range(1, c.numBars):

            self.thing = sim.send_box(x=0, y=l, z=0, length=0.05, width=30, height=c.heightBars)







