table <- read.csv("../Resources_k/df_all_k.csv")
lm(fire_size ~ Temp_pre_7 + Hum_pre_7 + Wind_pre_7, data=table)
summary(lm(fire_size ~ Temp_pre_7 + Hum_pre_7 + Wind_pre_7, data=table))

log_y <- log10(table$fire_size)

lm(log_y ~ Temp_pre_7 + Hum_pre_7 + Wind_pre_7, data=table)
summary(lm(log_y ~ Temp_pre_7 + Hum_pre_7 + Wind_pre_7, data=table))


#create histogram for original distribution
hist(table$fire_size, col='steelblue', main='Original')

#create histogram for log-transformed distribution 
hist(log_y, col='coral2', main='Log Transformed')



table(table$year,table$discovery_month)#generate contingency table

tbl <- table(table$year,table$discovery_month) #generate contingency table
chisq.test(tbl) #compare categorical distributions


table(table$year,table$fire_size_bin) #generate contingency table

tbl <- table(table$year,table$fire_size_bin) #generate contingency table
chisq.test(tbl) #compare categorical distributions


table(table$year,table$fire_cause) #generate contingency table

tbl <- table(table$year,table$fire_cause) #generate contingency table
chisq.test(tbl) #compare categorical distributions
