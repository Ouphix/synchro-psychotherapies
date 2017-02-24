library(lme4)
set.seed(5)
x <- floor(20*rnorm(15))+60
y <- floor(20*rnorm(15))
x1 <- x
x2 <- x+y+7
dt <- data.frame(1:15, x1,x2)
names(dt)[1]<- "sujet"
dt
dt1 <- reshape(dt, idvar = "sujet", varying=2:3, v.names="score", timevar="temps", direction="long")
dt1
dt1$sujet <- as.factor(dt1$sujet)
t.test (x1, x2, paired=TRUE, data=dt)
dt
summary(lm(score~temps+sujet, data=dt1))
summary(lmer(score~temps+(1|sujet), data=dt1))
