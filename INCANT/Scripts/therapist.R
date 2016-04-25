# INCANT study Data
# Therapist
getwd()
setwd("/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/")

therapist <- read.csv2("CSV/therapist.csv")
therapist
dim(table(therapist))

numpatients <- function(){
  x <- c()
  for (i in 1:4){
    table(therapist)[,i]
    x <-c(x,(length(which(table(therapist)[,i]!=0))))
  }
  names(x) <- c("Bastard", "Bonnaire", "Bouthillon", "Lascaux")
  x <- sort(x, decreasing = TRUE)
  return (x)
}


vect <-numpatients()
vect
barplot(vect, col= "#009999", las=1, ylim=c(0,16), main="Number of Patients by therapist")

