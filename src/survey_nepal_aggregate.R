library(ggplot2)
library(plyr)
library(dplyr)
path<- "/Users/ldolberg/Dropbox/Work/the_port_ors_hdx/data/nepal/F/CFP_Nepal_R2.csv"
df<-read.csv(path,header = TRUE,sep=";")
data1<- df %>% filter(Gender=="female" || Gender =="male") %>%
  group_by(District,Gender,Q1.i) %>% 
  summarize(total=n()) %>%
  mutate( ra = row_number(-total)) %>% filter(ra < 4)
data2<- df %>% group_by(District,Gender,Q2.i) %>% summarize(total=n()) %>%mutate( ra = dense_rank(-total))
data3<- df %>% group_by(District,Gender,Q3.i) %>% summarize(total=n()) %>%mutate( ra = dense_rank(-total))

p <- ggplot(data1,aes(x=Q1.i,y=total))+ geom_point() + facet_grid(District~Gender)
p

