library(RJDBC)
library(ggplot2)
library(ggmap)
library(googleVis)
drv <- JDBC("oracle.jdbc.OracleDriver",classPath="/Users/ldolberg/ojdbc6.jar", " ")



con <- dbConnect(drv, "jdbc:oracle:thin:@rdi-celpe-base.cucmtsxr0sac.eu-west-1.rds.amazonaws.com:1521:rdicelpe", "equipe_ri", "rdicelpe")

query <-"SELECT t3_users.CODE_L2_FEEDER as NAME,
       t3_users.users_PER_L2_FEEDER users, 
       COALESCE(inspected.users_inspected,0)/t3_users.users_PER_L2_FEEDER as INSPECTED_PERCENTAGE, 
COALESCE(fraud_users.fraud_inspected/COALESCE(t3_users.users_PER_L2_FEEDER,1),0) as FRAUD_PROPORTION,
COALESCE(fraud_users.kwh_recovered,0) as KWH_RECOVERED,
COALESCE(fraud_users.kwh_recovered/ COALESCE(inspected.users_inspected,1),0) as KWH_RECOVERED_PER_INSPECTION,
t3_users.KWH,
coords.X,
coords.Y
FROM (
SELECT uc.CODE_L2_FEEDER,          
count(distinct uc.ID_UC) as users_PER_L2_FEEDER,
avg(rc.MEASURED_CONSUMPTION) as KWH
FROM  RI_ENERGY.VW_RDI_UC uc
join RI_ENERGY.VW_RDI_CONSUMPTIONS rc
on rc.ID_UC=uc.ID_UC
GROUP BY uc.CODE_L2_FEEDER) t3_users
--WHERE uc.ID_UC in (select ic.ID_UC from  RI_ENERGY.VW_RDI_UC ic where ic.CODE_L2_FEEDER = uc.CODE_L2_FEEDER)
LEFT OUTER JOIN (
SELECT uc.CODE_L2_FEEDER, 
count(distinct uc.ID_UC) as users_inspected
FROM  RI_ENERGY.VW_RDI_UC uc 
WHERE  uc.ID_UC in (select distinct ic.ID_UC from RI_ENERGY.VW_RDI_INSPECTIONS ic )
GROUP BY uc.CODE_L2_FEEDER) inspected 
on inspected.CODE_L2_FEEDER = t3_users.CODE_L2_FEEDER
LEFT OUTER JOIN (
SELECT CODE_L2_FEEDER, count(distinct uc.ID_UC) fraud_inspected, 
sum(IC.ENERGY_RECOVERED) kwh_recovered
FROM  RI_ENERGY.VW_RDI_UC uc
left outer join RI_ENERGY.VW_RDI_INSPECTIONS IC
on  uc.ID_UC = ic.ID_UC 
where IC.INSPECTION_STATUS in ('FR','IR') 
GROUP BY uc.CODE_L2_FEEDER) fraud_users
on fraud_users.CODE_L2_FEEDER = t3_users.CODE_L2_FEEDER
LEFT OUTER JOIN (
SELECT CODE_L2_FEEDER, AVG(uc.COORD_LAT) as X, 
AVG(uc.COORD_LON) as Y
FROM  RI_ENERGY.VW_RDI_UC uc
WHERE uc.COORD_LON<> 0 AND uc.COORD_LAT <> 0 
GROUP BY uc.CODE_L2_FEEDER) coords 
on coords.CODE_L2_FEEDER = t3_users.CODE_L2_FEEDER
order by USERS desc,FRAUD_PROPORTION desc"
topquery <- sprintf("SELECT * FROM (%s) WHERE ROWNUM < %s",query,250)
tdf <- dbGetQuery(con,topquery)
gdf <-data.frame("LatLong"=sprintf("%.5f:%.5f",tdf$Y,tdf$X),"Tip"=sprintf("L2 Feeder=%s<BR>Users=%s<BR>Inspected=%.2f<BR>Fraud=%.2f<BR>KWH=%.2f<BR>KWH Recovered=%.2f",tdf$NAME, tdf$USERS,tdf$INSPECTED_PERCENTAGE,tdf$FRAUD_PROPORTION,tdf$KWH,tdf$KWH_RECOVERED))
M1 <- gvisMap(gdf,  "LatLong", "Tip", 
              options=list(showTip=TRUE, showLine=F, enableScrollWheel=TRUE, 
                           mapType='map', useMapTypeControl=TRUE, width=800,height=600))
plot(M1)
#q <- get_map(location= "Recife",zoom=11)
#ggmap(q)+geom_point(data=tdf,aes(y=Y,x=X,color=INSPECTED_PERCENTAGE,type=KWH))