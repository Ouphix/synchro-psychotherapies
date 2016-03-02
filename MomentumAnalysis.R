# Set direction
getwd()
setwd ("/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/CSV/")

# Functions
as.numeric.factor <- function(x){
  as.numeric(levels(x))[x]
}

## Import files
importdata <-function(fileslist){
    data <- c()
    for (i in list){
        dataAlone <-read.csv(i)
        print(i)
        data <- rbind(data, dataAlone)}
    return (data)
}

getwd()
importDataSeparated <- function(fileslist){
  for (i in list){
    print(i)
    importDataSeparated <-read.csv(i)
    return (importDataSeparated)
  }}
  
a <- importDataSeparated(list)

## Files list
list <- list.files("csvF104422022016", full.names=TRUE)
list

indexlist <- c("F1044C.VOB","F1044D1.VOB","F1044D2.VOB","F1044E.VOB","F1044F.VOB",
               "F1044G.VOB","F1044H.VOB","F1044I.VOB","F1044L.VOB","F1044M1.VOB",
               "F1044M2.VOB","F1044N.VOB", "F1044O.VOB", "F1044P.VOB", "F1044Q.VOB",
               "F1044R1.VOB","F1044R2.VOB")

labelvideolist<- c("C","D1","D2","E","F", "G","H","I","L","M1", "M2","N", "O", "P", "Q",
                   "R1","R2")

colOrderList <- c("blue","red", "green","orange")

#Import data
data <- importdata(list)

ParticipantsList <- names(data[,2:5])
print(ParticipantsList)

# Dim of data data.frame
summary(data)
str(data)

# Set the variables after modifyinfg in excel
#data$father <- as.numeric.factor(data$father)
#data$mother <- as.numeric.factor(data$mother)
#data$patient <- as.numeric(data$patient)
#data$therapist <- as.numeric.factor(data$therapist)

# ----------------------------

# Create time in minutes x axis
data$timeMin <- data$frame/(25*60)
# plot(data$timeMin)
# Frame rate 25/sec. Check with the other settings

# -------------------------------

# Length of the video in min
videoLengthList <-c()
for (i in indexlist){
  index<-which(data$file==i)
  videolength <- max (data$timeMin[index])
  videoLengthList <-c(videoLengthList,videolength)
}

print(videoLengthList)

par(mar=c(4,4,3,1))
barplot(videoLengthList, col="cornflowerblue", cex.axis=0.6, cex.names=0.6,
        ylab="Minutes", xlab="Video Name", las=1, names=labelvideolist, 
        main="Length in each F1044 video (min)")
        abline(h = mean(videoLengthList), lwd=2, lty=2)
        text(20,20, "Mean")

# ----------------------------

# Number of lines of the file (frame) for each video
## sort(table(data$file), decreasing = TRUE)
barplot(table(data$file), col="cornflowerblue", cex.axis=0.6, cex.names=0.5, cex.lab=0.8,
        main="Number of frames in each F1044 video", cex.main=0.8, ylab="Frame number", 
        names = labelvideolist, xlab="Video Name", las=1)

# --------------------------

# How many NA for each subject
tab <- cbind(table(is.na(data[,2])),table(is.na(data[,3])),table(is.na(data[,4])), 
                                                          table(is.na(data[,5])))
tab

par(mar=c(3,3,2,1))
barplot(tab, cex.axis = 0.7, las=2, cex.main= 1, names=ParticipantsList, 
  main="Number of available data by subject", 
  beside=TRUE, las=1, col=terrain.colors(2), ylim=c(0,600000))
legend("topright", c("T", "F"), fill=terrain.colors(2))

#Mother and therapist are more often present

------------------------------------------------
# Description of the data
meanMomentumList <-c()
meanMomentum <- function(subject){
    for (i in indexlist){
              index <- which(data$file==i)
              print(length(data[index,subject]))
              print(summary(data[index,subject]))
              momentumsubject<- mean(data[index,subject], na.rm=TRUE)
              meanMomentumList <-c(meanMomentumList, momentumsubject)
    }
  return (meanMomentumList)
}

momentumfatherlist <- meanMomentum("father")
momentumMotherList <- meanMomentum("mother")
momentumTherapistList <- meanMomentum("therapist")
momentumPatientList <- meanMomentum("patient")

momentumMeanList <- rbind(momentumfatherlist, momentumMotherList, momentumPatientList, momentumTherapistList)

dim(momentumMeanList)
momentumMeanList

par(mar=c(3,3,2,1))
barplot(momentumMeanList, names=labelvideolist, las=1, cex.axis = 0.4, cex.names=0.6, 
        main="Mean Momentum in each video", beside=TRUE, 
        col=colOrderList)
par(mar=c(1,0.5,0.5,1))
legend("top", inset=.05, ParticipantsList, 
       fill=colOrderList, cex=0.7)

# Momentum box plots by frame
par(mar=c(3,3,2,2))
boxplot(data$father, data$mother, data$therapist, data$patient, 
        col=colOrderList, 
        names=ParticipantsList, 
        main= "Momentum by frame box plots ", las=1)
par(mar=c(1,0.5,0.5,1))
legend("topleft", ParticipantsList, fill=colOrderList, cex=0.7)

summary(data$father)

# Simplifing this vector, with mean in each interval
## subject_momentum = vector of momentum

## interval = number of frames by interval 25 for one second, 1500 for one minute
MeanMomentumByTime <- function(subject, interval, data){
  x <- c()
  for (file in indexlist){
       # print(file)
    #  print(data[which(data$file==file), subject])
        dataVector <- data[which(data$file==file), subject]
        ## with ceiling : superior limit of the round
        IntervalNumbersVideo <- ceiling(length(dataVector)/interval)
        for (i in 1:IntervalNumbersVideo){
                borneinf<- 1+(i-1)*interval
               # print (borneinf)
                bornesup <-i*interval
               # print (bornesup)
                dataVectorInterval <- dataVector[borneinf:bornesup]
                mean <- mean(dataVectorInterval, na.rm=TRUE)
                x <- c(x, mean)
         }
    #    print (tail(x))
        }
  return (x)
}

# Example by Minute
fatherMinute <- MeanMomentumByTime("father", 1500, data)
motherMinute <- MeanMomentumByTime("mother", 1500, data)
therapistMinute <- MeanMomentumByTime("therapist", 1500, data)
patientMinute <- MeanMomentumByTime("patient", 1500, data)

str(fatherMinute)

#Plot the Mean Momentum by time each minute to detect abberant moves
par(mar=c(3,3,2,2))
plot(1:325,fatherMinute, type="l", main="Mean Momentum by minute, all F1044 videos", col="blue")
lines(motherMinute, col="red")  
lines(therapistMinute, col="orange")
lines(patientMinute, col="green")
legend("topleft", ParticipantsList , fill=colOrderList, cex=0.7)

# To do :
# Export graphs for each video wit h appropriate title, appropriate, length

##Functions that takes data and return the plots by minutes of each video
data <- 
par(mar=c(4,4,4,2))
for (i in 1:length(labelvideolist)){
  videoindex <- labelvideolist[i]
  videoFullname <- indexlist[i]
  filename <- paste("MeanMomentumMinute", videoindex, ".pdf", sep = "")
  # pdf(filename)
  fatherMinute <- MeanMomentumByTime("father", 1500, data)
  motherMinute <- MeanMomentumByTime("mother", 1500, data)
  therapistMinute <- MeanMomentumByTime("therapist", 1500, data)
  patientMinute <- MeanMomentumByTime("patient", 1500, data)
  
  # dev.off()
}

SlidingInterval <- function(subject, interval, data){
  x <- c()
  for (file in indexlist[1]){
    print(file)
    dataVector <- data[which(data$file==file), subject]
    print (length(dataVector))
    NBofAnalysedframes <- length(dataVector)-interval+1
    for (i in 1:NBofAnalysedframes){
      borneinf<- (i)
      print (borneinf)
      bornesup <-(interval-1+i)
      print (bornesup)
      dataVectorInterval <- dataVector[borneinf:bornesup]
      mean <- mean(dataVectorInterval, na.rm=TRUE)
      x <- c(x, mean)
    }
    print (tail(x))}
  return (x)
}

slidedfather <- SlidingInterval("father",11, data)
str(slidedfather)

par(mar=c(4,4,4,2))
plot(1:250, data$father[251:500], main="Mean Momentum (Sliding 11 frames interval) 
     for father on F1044C video, 10 seconds ", xlab="Frame index (25/s)", ylab="Momentum",
     col="red", type="l")
lines(slidedfather[251:500],  col="blue")
legend("topleft", c("Raw data", "Mean on sliding Interval") , fill=c("red", "blue"), cex=0.7)

fatherEleven<- MeanMomentumByTime("father", 11, data)

plot (23:46, fatherEleven[23:46], type="l", col="orange", main="Mean Momentum (non overlapping 11 frames
      intervals) for father on F1044C video, between 10-20 seconds", ylab="Momentum", xlab="Frame index (each 11 frames)" )
legend("topleft", c("Mean on 11 frame interval") , fill=c("orange"), cex=0.7)


length(fatherEleven)

datafatherF1044C <- data[which(data$file=="F1044C.VOB"), "father"]
str(datafatherF1044C)
summary(datafatherF1044C)

par(mar=c(3,3,2,2))

str(datafatherF1044C)

# Momentum box plots by second
par(mar=c(3,3,2,2))
boxplot(fatherSecond, motherSecond, therapistSecond, patientSecond, 
        col=colOrderList, names=ParticipantsList , 
        cex.axis=0.7, cex.names=0.6,
        main= "Mean Momentum by second box plots ", las=1)
par(mar=c(1,0.5,0.5,1))

# Momentum plot by second
par(mar=c(4,4,2,2))
plot(fatherSecond, type="l", col="blue", ylab="Momentum", 
     main="Momentum for F1044 video by second", las=1, cex.axis=0.7)
lines(motherSecond, col="red")  
lines(therapistSecond, col="orange")
lines(patientSecond, col="green")
legend ("bottomright", legend=c("patient", "therapist", "father", "mother"), col=c("green", "orange", "blue", "red"),lty=c(1,1), lwd=3, cex=0.5)

# Example by minute
length(data$father)

fatherMinute <- MeanMomentumByTime(data$father, 1500)
motherMinute <- MeanMomentumByTime(data$mother, 1500)
therapistMinute <- MeanMomentumByTime(data$therapist, 1500)
patientMinute <- MeanMomentumByTime(data$patient, 1500)

par(mar=c(3,3,2,2))
boxplot(fatherMinute, motherMinute, therapistMinute, patientMinute, 
        col=colOrderList, names=ParticipantsList , 
        cex.axis=0.7, cex.names=0.6,
        main= "Mean Momentum by minute box plots ", las=1)
par(mar=c(1,0.5,0.5,1))
legend("topleft", ParticipantsList , 
       fill=colOrderList, cex=0.7)

par(mar=c(4,4,2,2))
plot(fatherMinute, type="l", col="blue", ylab="Momentum", 
     main="Momentum for F1044 video by second", las=1, cex.axis=0.7)
lines(motherMinute, col="red")  
lines(therapistMinute, col="orange")
lines(patientMinute, col="green")
legend ("bottomright", legend=ParticipantsList , col=colOrderList,lty=c(1,1), lwd=3, cex=0.5)


## max(therapist) = 0.004800465 to put in in the graph
plot(father, type="l", col="blue", ylim=c(0, 0.005), las=1, ylab="Momentum", main="Momentum for F1044C video by minute")
lines(mother, col="red")  
lines(therapist, col="orange")
legend ("topleft", legend=c("patient", "therapist", "father", "mother"), col=c("green", "orange", "blue", "red"),lty=c(1,1), lwd=3)

plot(data$timeMin, data$mother, type="l", col="red", xlab="Time (min)", ylab="Momentum", main="Momentum for F1044C video by frame")
lines(data$timeMin, data$father, col="blue")  
lines(data$timeMin, data$therapist, col="orange")
# lines(data$timeMin, data$patient, col="green") 
legend ("top", legend=c("patient", "therapist", "father", "mother"), col=c("green", "orange", "blue", "red"),lty=c(1,1), lwd=3)

# Plot density by frame
plot(density(data$mother, na.rm=TRUE),col="red", main="Density plot of momentum")
lines(density(data$father, na.rm=TRUE), col="blue")
lines(density(data$therapist, na.rm=TRUE), col="orange")
legend("topright",legend=c("father", "mother", "therapist"), col=c("blue", "red", "orange"),lty=1:1, lwd=3)

# Plot values
plot(data$timeMin, data$mother, type="l", col="red", xlab="Time (min)", ylab="Momentum", main="Momentum for F1044C video")
lines(data$timeMin, data$father, col="blue")  
lines(data$timeMin, data$therapist, col="orange")
# lines(data$timeMin, data$patient, col="green") 
legend ("top", legend=c("patient", "therapist", "father", "mother"), col=c("green", "orange", "blue", "red"),lty=c(1,1), lwd=3)

------
