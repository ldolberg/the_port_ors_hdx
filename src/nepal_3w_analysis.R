data.3w = read.csv("/home/danito/proj/hhton/the_port_ors_hdx/data/Nepal/humanitarian/nepal-3w-14july2015-consolidated.csv")

data.ww = read.csv("/home/danito/proj/hhton/the_port_ors_hdx/data/Nepal/humanitarian/who_what.csv")
data.fts = read.csv("/home/danito/proj/hhton/the_port_ors_hdx/data/Nepal/humanitarian/fts_nepal.csv")

require(ggplot2)
cont.organizations = ddply(data.ww, .(Organisation.Name), summarise, count=length(Cluster))
qplot(reorder(Organisation.Name,count), count, data=subset(cont.organizations, count > 86)) + theme(axis.text.x = element_text(angle = 90, hjust = 1))
qplot(Cluster, count, data=(ddply(data.ww, .(Cluster), summarise, count=length(Cluster))))

dim(subset(data.3w, !is.na(Targets))
dim(subset(data.3w, is.na(Targets))

dim(subset(data.3w, TOTAL >0))
dim(subset(data.3w, is.na(TOTAL)))
