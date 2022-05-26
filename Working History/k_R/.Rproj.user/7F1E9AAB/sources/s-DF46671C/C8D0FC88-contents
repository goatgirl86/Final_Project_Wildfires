library(dplyr)

cars <- read.csv("MechaCar_mpg.csv")

lm(mpg ~ vehicle_length + vehicle_weight + spoiler_angle 
   + ground_clearance + AWD, data=cars)


summary(lm(mpg ~ vehicle_length + vehicle_weight + 
             spoiler_angle + ground_clearance + AWD, data=cars))



#-------------------

coils <- read.csv("Suspension_Coil.csv")

total_summary <- summarize(coils, mean(PSI),median(PSI),var(PSI),sd(PSI))

lot_summary <- group_by(coils,Manufacturing_Lot)
lot_summary_df <- summarize(lot_summary, mean(PSI),median(PSI),var(PSI),sd(PSI))



#---------------------------

t.test((coils$PSI), mu = 1500)


coils
lot1 <- subset(coils, Manufacturing_Lot=="Lot1")
lot2 <- subset(coils, Manufacturing_Lot=="Lot2")
lot3 <- subset(coils, Manufacturing_Lot=="Lot3")

t.test((lot1$PSI), mu = 1500)
# 
t.test((lot2$PSI), mu = 1500)
# 
t.test((lot3$PSI), mu = 1500)

