## Evolutionary Robotics Final Project

P. Alexander Burnham

4, April 2018

#### Does robot joint and limb morphology affect evolutionary response using a distance-based fitness function?

Time Line: 4) Adjust fitness function and add and test rough environment:

This week I implemented a rough terrain treatment. I included constants that describe the number and height of raised bars to be placed between the robot and the light sensor. I called them into the simulator from the environment object using a for loop. The fitness function remains distance. I had imagined that I would need to add additional terms to the fitness function, however, a simple distance-based function yields satisfactory results and allows for a great deal of evolutionary freedom. In future, as I work on finishing this project, I may find that changes are necessary, at which point I will make modifications. 

The goal of the experiment is to observe how robot and terrain complexity affects the evolutionary timeline (fitness through time). To this end, a simple platform seems an adequate playing field for these different robots and their controllers. 

Shown below is the rough environment with 10 bars raised 0.1 units from the ground. The simulation shown in the video is the best controller from a run of 100 generations with a population of 10. You will notice, contrary to the flat landscape, the robot has developed a repetitive gate for hopping over the obstacles. 

**Image of rough terrain:**

![Screen Shot 2018-04-04 at 4.37.09 PM](/Users/phillipburnham/Desktop/Screen Shot 2018-04-04 at 4.37.09 PM.png)

**Video of robot rough terrain:**

https://www.youtube.com/watch?v=cNxLzkCxVGU&feature=youtu.be
