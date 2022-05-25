table <- read.csv("../Resources/temps_to_7.csv")
lm(fire_size ~ Temp_pre_30 + Hum_pre_30 + Wind_pre_30, data=table)
summary(lm(fire_size ~ Temp_pre_30 + Hum_pre_30 + Wind_pre_30, data=table))

log_y <- log10(table$fire_size)

lm(log_y ~ Temp_pre_30 + Hum_pre_30 + Wind_pre_30, data=table)
summary(lm(log_y ~ Temp_pre_30 + Hum_pre_30 + Wind_pre_30, data=table))


#create histogram for original distribution
hist(table$fire_size, col='steelblue', main='Original')

#create histogram for log-transformed distribution 
hist(log_y, col='coral2', main='Log Transformed')



table(table$year,table$discovery_month) #generate contingency table

tbl <- table(table$year,table$discovery_month) #generate contingency table
chisq.test(tbl) #compare categorical distributions
