#!/bin/bash
#This will find the file has been updated
key=`grep '^Authorization: ' config.txt`
lmod=`egrep '^Last-Modified:' runTime.txt`
lmod=`echo $lmod`
time=`curl -X GET --header  "$key" 'https://api.transport.nsw.gov.au/v1/publictransport/timetables/complete/gtfs' -I | egrep '^Last-Modified:' `
time=`echo $time`
if [ -z "$lmod" ]
then
    echo $time >> runTime.txt
    echo 'No previous update time discovered in runTime.txt'
    curl -X GET --header  "$key" 'https://api.transport.nsw.gov.au/v1/publictransport/timetables/complete/gtfs' > timetable.zip
    rm -rf ./timtable
    unzip timetable.zip -d ./timetable
    #This removes the old database
    rm ./transport.sqlite
    Rscript refreshDB.R
elif [ "$time" != "$lmod" ]
then  
    echo 'Previous version is out of date according to runTime.txt'
    sed "s/^Last-Modified:.*/$time/" runTime.txt > temp.$$
    cat temp.$$ > runTime.txt
    rm temp.$$
    curl -X GET --header  "$key" 'https://api.transport.nsw.gov.au/v1/publictransport/timetables/complete/gtfs' > timetable.zip
    rm -rf ./timtable
    unzip timetable.zip -d ./timetable
    #This removes the old database
    rm ./transport.sqlite
    Rscript refreshDB.R
fi
