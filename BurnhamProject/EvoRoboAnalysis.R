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

# read in data:
#BeeData <- read.table("2016_Bombus_Survey_Data.csv", header=TRUE, sep = ",", stringsAsFactors = FALSE) 

data1 <- scan("Robot3_Smooth/Robot3_Smooth.csv", sep=',', what = "", quiet = TRUE)
data1 <- as.numeric(data1)
#data1 <- na.omit(data1)
#dat <- data1[-c(1:868)]



# turn data set into a matrix of gen by n:
data1 <- as.vector(data1)
#names(data1) <- NULL
mat <- matrix(data1, ncol=30)

# calculate row means to get vector to plot by
rowMeans(mat)

plot(1:199,rowMeans(mat))





ggplot(data, aes(x=Generations, y=Fitness, color=Treatment)) + geom_line(size = 2) + 
  theme_bw(base_size = 17) + theme(legend.position=c(.2, .8))

