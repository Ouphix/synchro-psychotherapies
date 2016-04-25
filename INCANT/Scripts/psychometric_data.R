# Import library to read excel files
library(xlsx)

CBCL <- read.xlsx("./CSV/psychometry/CBCL_INCANT.xls", 1)
str(CBCL)
View(CBCL)


TLFB <- read.csv2("./CSV/psychometry/TLFB_INCANT.csv")
str(TLFB)
View(TLFB[,c(1, 25:29)])



class(TLFB[1,c(25:29)])

rainbow(length(TLFB$Case))[1]

plot <- FALSE
for (i in 1:length(TLFB$Case)){
  v <- as.numeric(as.vector(TLFB[i,c(25:29)]))
  if (plot==FALSE){
        plot(v, type="l", col=rainbow(length(TLFB$Case))[i])
        plot <- TRUE}
  else{
    print(TLFB$Case[i])
    print(i)
    plot(v, col=rainbow(length(TLFB$Case))[i])}}

length(TLFB)

View(TLFB)

YSR <- read.xlsx("./CSV/psychometry/YSR_INCANT.xls", 1)
str(YSR)
View(YSR)
