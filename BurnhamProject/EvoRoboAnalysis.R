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
data <- read.table("TestData.csv", header=TRUE, sep = ",", stringsAsFactors = FALSE) 
data1 <- read.table("output.csv", sep = ",", stringsAsFactors = FALSE)

# turn data set into a matrix of gen by n:
data1 <- as.vector(data1)
names(data1) <- NULL
data1 <- as.numeric(data1)
mat <- matrix(data1, ncol=4)

# calculate row means to get vector to plot by
rowMeans(mat)






ggplot(data, aes(x=Generations, y=Fitness, color=Treatment)) + geom_line(size = 2) + 
  theme_bw(base_size = 17) + theme(legend.position=c(.2, .8))

