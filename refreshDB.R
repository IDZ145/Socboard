library("DBI")
library("RSQLite")
con = dbConnect(RSQLite::SQLite(), dbname="transport.sqlite")


files <- list.files(path = "./timetable", pattern = "[.]txt$")


for(i in files){
    data <- substr(i,1,nchar(i)-4)
    filePath <- paste(c("./timetable/",i),sep="",collapse="")
    print(filePath)
    dataTable <- read.csv(file=filePath,head=TRUE,sep=",")
    dbWriteTable(con, data, dataTable, overwrite = TRUE)
}