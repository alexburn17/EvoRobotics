## Evolutionary Robotics Final Project

P. Alexander Burnham

23, February 2018



#### Does robot joint an limb morphology affect evolutionary response to the same distance based fitness function?

In this study I propose to create four robot types (multi-jointed vs single-jointed and horizontal vs vertical joint normals in a 2 by 2 factorial design) utilizing similar structures and the same evolutionary algorithm, environment and fitness function. The goals are to evolve a robot that can maximize its fitness by walking the farthest from its point of origin and statistically quantify how morphological differences can assist or handicap a robot during the evolutionary process. 

**Questions:**

Do robots that use similar but distinct morphologies respond differently to the same evolutionary pressures?

How robust are these different forms to changes in the roughness of the environment?

**Hypotheses:** 

I predict that robots with few horizontal joints will respond to evolutionary more readily than the other morphologies, but suffer in robustness by being overfitted to a particular landscape. 

#### Time Line:

1) Create robots one and two that are single jointed.

2) Create robots three and four that use two joints.

3) Refine the hillclimber algorithm 

4) Optimize fitness function and create smooth and rough environments 

5) Develop a nested protocol to take evolved ANNs and use them to begin the next round of evolution

6) Work on combing all of these elements into an object based program

7) Run the simulations for all robots in all terrains

8) Data Analysis 



