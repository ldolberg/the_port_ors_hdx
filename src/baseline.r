require(plyr)
setwd("")
data.base.1 = subset(read.csv("~/proj/hhton/the_port_ors_hdx/data/Nepal/baseline/earthquake_impact.csv"))
data.base.2 = subset(read.csv(
  "~/proj/hhton/the_port_ors_hdx/data/Nepal/baseline/npl-popt-adm4-2011-wfp.csv"),
  select = -c(SURVEY_NAM, VDC_ID, VDC_NAME, REGION))
names(data.base.2)[3] = "ZONE"

data.baseline = rbind(melt(data.base.1, id.vars = c("DIST_ID", "ZONE", "DISTRICT")),
melt(data.base.2, id.vars = c("DIST_ID", "ZONE", "DISTRICT")))

data.baseline = data.baseline[,c(-1, -2)]
data.baseline$variable = sub(pattern = "Total.Household", replacement = "housing", x=data.baseline$variable)
data.baseline$variable = sub(pattern = "Tot_Deaths", replacement = "health", x=data.baseline$variable)
data.baseline$variable = sub(pattern = "PublicBuild_Damage", replacement = "finantial", x=data.baseline$variable)


