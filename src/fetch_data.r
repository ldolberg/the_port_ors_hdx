#In case the package is not installed
#install.packages("rjson")

#Import the rjson package
library("rjson")
library("assertthat")
#URL Point to the dataset 
json_file <- "https://data.hdx.rwlabs.org/api/action/package_list?id=data_explorer"

#Retrieve the data and parse it
json_data <- fromJSON(paste(readLines(json_file), collapse=""))
stopifnot(json_data$success)

results <- json_data$result
cat(length(results))
#Filter Ocha Datasets
ocha_datasets <- results[grep("ocha",results)]

#Filter Specific ORS Key Figure Datasets
ors_key <- results[grep("ors-key-figure",results)]

#Get the information related to the ORS Key Figures
ors_file <- sprintf("https://data.hdx.rwlabs.org/api/action/package_show?id=%s",ors_key)
ors_data <- fromJSON(paste(readLines(ors_file), collapse=""))
stopifnot(ors_data$success)

#Get the tags of datasets matching ors
ors_tags_action <- sprintf("https://data.hdx.rwlabs.org/api/3/action/tag_show?id=%s","ors")
ors_tags <- fromJSON(paste(readLines(ors_tags_action), collapse=""))
stopifnot(ors_tags$success)





