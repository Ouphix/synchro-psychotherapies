#Videos
#number of videos by patient
# X, y position 
# locator(1) 

getwd()
setwd("CSV")
videos <-read.csv2("videos.csv")

tab <- table(videos$NumPatient)
tab
tabsort <- sort(tab, decreasing = TRUE)

length(tabsort)
meanvideos <- mean(table(videos$NumPatient))

par(mfrow=c(2,1), mar=c(4,3,2,2))
barplot(tabsort[1:16], cex.axis = par("cex.axis"), col="cornflowerblue", cex=1, las=2,
        main="Number of videos by patient",  ylim=c(0, 20))
abline(h = mean(table(videos$NumPatient)), lwd=2, lty=2)
text(17,6, "Mean")

barplot(tabsort[16:32], cex.axis = par("cex.axis"), col="cornflowerblue", cex=1, las=2,
        ylim=c(0, 10))
abline(h = meanvideos, lwd=2, lty=2)
text(18,4.5, "Mean")

par(mar=c(4,3,2,2))
barplot(tabsort, cex.axis = par("cex.axis"), col="cornflowerblue", cex=0.8, las=2,
        main="Number of videos by patient",  ylim=c(0, 20))
abline(h = mean(table(videos$NumPatient)), lwd=2, lty=2)
text(35,5, "Mean")


