import constants as c
import pyrosim

class ENVIRONMENT:
    def __init__(self, e):
        # Environment ID
        self.ID = e

        self.l = c.L
        self.w = c.L
        self.h = c.L

        if self.ID == 0:
            self.Place_Light_Source_To_The_Front()
        elif self.ID == 1:
            self.Place_Light_Source_To_The_Right()
        elif self.ID == 2:
            self.Place_Light_Source_To_The_Back()
        elif self.ID == 3:
            self.Place_Light_Source_To_The_Left()

        #print(self.l,self.w,self.h,self.x,self.y,self.z)

    def Place_Light_Source_To_The_Front(self):

        self.x = c.L * 0
        self.y = c.L * 30
        self.z = c.L * 0

    def Place_Light_Source_To_The_Right(self):

        self.x = c.L * 30
        self.y = c.L * 0
        self.z = c.L * 0

    def Place_Light_Source_To_The_Back(self):

        self.x = c.L * 0
        self.y = c.L * -30
        self.z = c.L * 0

    def Place_Light_Source_To_The_Left(self):

        self.x = c.L * -30
        self.y = c.L * 0
        self.z = c.L * 0

    def Send_To(self, sim):
        lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h)
        sim.send_light_source(body_id=lightSource)





