# convert xls files in CSV files
getwd()
# select working directory
setwd("/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/INCANT/Data/CSV/psychometry")
# list files in this directory
listFiles <- list.files("./")
# print this list
listFiles

# import xlsx library to read excel files
library(xlsx)

# load the data bases
CBCL <- read.xlsx("CBCL_INCANT.xls", sheetIndex = 1)
TLFB <- read.xlsx("TLFB_INCANT.xls", sheetIndex = 1)
YSR <- read.xlsx("YSR_INCANT.xls", sheetIndex = 1)

# merge the data bases by Case column
data2 <-merge(CBCL, TLFB, by="Case")
data <- merge(data2, YSR, by="Case")

# Present the resulted data frame
str(data)
dim(data)
View(data)

# Delete useless columns
data$Country.x <-NULL
data$Country.y <- NULL
data$Country
names(data)
dataCannabis <- data.frame (data$Case , data$Q18_3_0,data$Q18_3_3, data$Q18_3_6, data$Q18_3_9, data$Q18_3_12)
dataCannabis
write.csv(data, file="dataINCANT.csv")
write.csv(dataCannabis, file="dataCannabis.csv")
read.csv("dataINCANT.csv")
