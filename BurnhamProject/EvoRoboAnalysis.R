###########################################################################################
# Data Analysis Evolutionary Robotics Project
# P. Alexander Burnham
# April 12, 2018
###########################################################################################

#Preliminaries:
# Clear memory of characters
ls()
rm(list=ls())

# Call Required Packages
library("ggplot2")
library("dplyr")
library("plyr")
library("lme4")
library("car")

# Set Working Directory: 
setwd("~/EvoRobotics/BurnhamProject")

# read in data from 8 files from evo runs
data1 <- scan("Robot1_Smooth/Robot1_Smooth.csv", sep=',', what = "", quiet = TRUE)
data2 <- scan("Robot1_Rough/Robot1_Rough.csv", sep=',', what = "", quiet = TRUE)
data3 <- scan("Robot2_Smooth/Robot2_Smooth.csv", sep=',', what = "", quiet = TRUE)
data4 <- scan("Robot2_Rough/Robot2_Rough.csv", sep=',', what = "", quiet = TRUE)
data5 <- scan("Robot3_Smooth/Robot3_Smooth.csv", sep=',', what = "", quiet = TRUE)
data6 <- scan("Robot3_Rough/Robot3_Rough.csv", sep=',', what = "", quiet = TRUE)
data7 <- scan("Robot4_Smooth/Robot4_Smooth.csv", sep=',', what = "", quiet = TRUE)
data8 <- scan("Robot4_Rough/Robot4_Rough.csv", sep=',', what = "", quiet = TRUE)
randomDat <- scan("Random.csv", sep=',', what = "", quiet = TRUE)


####################################################################
# Function: fitnessCurv
# Takes data from each evolutionary run of 30 from pyrosim
# and turns it into a clean numeric matrix 30 runs for 199 gens
# INPUT: data = char string
# OUTPUT: clean matric of type numeric 
####################################################################

fitnessCurv <- function(data=data){
# make char data numeric
data <- as.numeric(data)

# turn data set into a matrix of gen by n:
data <- as.vector(data)

# names(data1) <- NULL
mat <- matrix(data, ncol=30)

return(mat)

}
#####################################
##### END FUNCTINON #################
#####################################

# run function on each file
mat1 <- fitnessCurv(data1)
mat2 <- fitnessCurv(data2)
mat3 <- fitnessCurv(data3)
mat4 <- fitnessCurv(data4)
mat5 <- fitnessCurv(data5)
mat6 <- fitnessCurv(data6)
mat7 <- fitnessCurv(data7)
mat8 <- fitnessCurv(data8)

# merge data
mat <- rbind(mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8)

# calculate row means to get vector to plot by
fitMeans <- rowMeans(mat)

# create variable for terrain type
Landscape <- c(rep("Smooth", 199), rep("Rough", 199), rep("Smooth", 199), rep("Rough", 199), rep("Smooth", 199), rep("Rough", 199), rep("Smooth", 199), rep("Rough", 199))

# creat variable for robot type
Robot <- c(rep("Robot1", 199), rep("Robot1", 199), rep("Robot2", 199), rep("Robot2", 199), rep("Robot3", 199), rep("Robot3", 199), rep("Robot4", 199), rep("Robot4", 199))

# create number of generations counter
Generations <- rep(1:199, 8)

# create data frame:
DF <- data.frame(Generations, Landscape, Robot, fitMeans)

str(DF)

DF$Landscape <- factor(DF$Landscape, levels = c("Smooth", "Rough"))

# Fitness plot
ggplot(DF, aes(x=Generations, y=fitMeans, color=Robot, linetype =Landscape)) + geom_line(size = 2) + theme_bw(base_size = 17) + labs(x="Time (generations)", y="Fitness (light intensity)") + theme(legend.key.width = unit(2.5, "line"))



####################################################################
# Function: maxFunc
# Takes data from each evolutionary run of 30 from pyrosim
# and find the gen number when fitness first is max
# INPUT: data = matrix of gen by N
# OUTPUT: vetor of generation numbers
####################################################################

# find max value in each column
maxFunc <- function(data=data){

# pre allocate vector for    
max1 <- numeric(dim(data)[2])

for (i in 1:30){
max1[i] <- which.max(data[,i])
}

return(max1)
}

#####################################
##### END FUNCTINON #################
#####################################



####################################################################
# Function: maxFuncFit
# Takes data from each evolutionary run of 30 from pyrosim
# and find the fitness max for each column
# INPUT: data = matrix of gen by N
# OUTPUT: vetor of max fitness values
####################################################################

# find max value in each column
maxFuncFit <- function(data=data){
  
  # pre allocate vector for    
  max1 <- numeric(dim(data)[2])
  
  for (i in 1:30){
    max1[i] <- max(data[,i])
  }
  
  return(max1)
}

#####################################
##### END FUNCTINON #################
#####################################


# find max number of gens for each of 8 treatments:
maxGens <- c(maxFunc(mat1), maxFunc(mat2), maxFunc(mat3), maxFunc(mat4), maxFunc(mat5), maxFunc(mat6), maxFunc(mat7), maxFunc(mat8), rep(NA, 240))

# find max fitness for each of 8 treatments:
maxFit <- c(maxFuncFit(mat1), maxFuncFit(mat2), maxFuncFit(mat3), maxFuncFit(mat4), maxFuncFit(mat5),maxFuncFit(mat6), maxFuncFit(mat7), maxFuncFit(mat8), randomDat)
maxFit <- as.numeric(maxFit)

# create variable for terrain type
Landscape <- c(rep("Smooth", 30), rep("Rough", 30), rep("Smooth", 30), rep("Rough", 30), rep("Smooth", 30), rep("Rough", 30), rep("Smooth", 30), rep("Rough", 30))
Landscape <- c(Landscape, Landscape)

# creat variable for robot type
Robot <- c(rep("Robot1", 30), rep("Robot1", 30), rep("Robot2", 30), rep("Robot2", 30), rep("Robot3", 30), rep("Robot3", 30), rep("Robot4", 30), rep("Robot4", 30))
Robot <- c(Robot, Robot)

RunType <- c(rep("Evolutionary Algorithm", 240), rep("Random Controller", 240))

ID <- c(1:240)

# merge into a dataframe:
genData <- data.frame(RunType, Landscape, Robot, maxGens, maxFit, ID)












genDataSplit <- genData[genData$RunType=="Evolutionary Algorithm", ]
#ddply summarize:
Temp <- ddply(genDataSplit, c("Robot", "Landscape"), summarise, 
              n = length(maxGens),
              mean = mean(maxGens, na.rm=TRUE),
              sd = sd(maxGens, na.rm=TRUE),
              se = sd / sqrt(n))

#choosing color pallet
colors <- c("blue", "grey")

#creating the figure of max gens:
plot1 <- ggplot(Temp, aes(x=Robot, y=mean, fill=Landscape)) +
  geom_bar(stat="identity",
           position=position_dodge()) + labs(y="Gens to Max Fitness", x="Robot Type") + geom_errorbar(aes(ymin = mean - se, ymax = mean + se, width = 0.2),position=position_dodge(.9))

plot1 + theme_minimal(base_size = 17) + theme(legend.position=c(.9, .9)) + scale_fill_manual(values=colors) + coord_cartesian(ylim = c(0, 200)) 






# calculate mean of random runs:
genDataRandom <- genData[!genData$RunType=="Evolutionary Algorithm", ]
mean(genDataRandom$maxFit)

#ddply summarize:
Temp1 <- ddply(genDataSplit, c("Robot", "Landscape", "RunType"), summarise, 
              n = length(maxFit),
              mean = mean(maxFit, na.rm=TRUE),
              sd = sd(maxFit, na.rm=TRUE),
              se = sd / sqrt(n))

#choosing color pallet
colors <- c("blue", "grey")

#creating the figure of max gens:
plot1 <- ggplot(Temp1, aes(x=Robot, y=mean, fill=Landscape)) +
  geom_bar(stat="identity",
           position=position_dodge()) + labs(y="Max Fitness", x="Robot Type") + geom_errorbar(aes(ymin = mean - se, ymax = mean + se, width = 0.2),position=position_dodge(.9))

plot1 + theme_minimal(base_size = 17) + theme(legend.position=c(.9, .9)) + scale_fill_manual(values=colors) + coord_cartesian(ylim = c(0, 0.4)) + annotate("segment", x = 0.5, xend = 4.5, y = mean(genDataRandom$maxFit) , yend = mean(genDataRandom$maxFit), colour = "red", size=1)

# analysis of max gens
kruskal.test(data = genData, maxFit ~ Robot)

mod <- glmer(data=genDataSplit, maxFit ~ Robot * Landscape + (1|Robot), family = Gamma)
summary(mod)

mod1 <- glmer(data=genDataSplit, maxGens ~ Robot * Landscape + (1|Robot), family = Gamma)
summary(mod1)

