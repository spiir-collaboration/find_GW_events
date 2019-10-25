# find_GW_events
To search within a given set of time windows around a set of times of interest (eg. times of electromagnetic triggers)

Files/folders in folder:
data/
ranges.txt
search_many_times.py
search_time.py
times.txt

How to run:
1. Open times and fill with the times around which you want to search. Put times in as GPS integer times, with a new line for each time. Format of each line:XXXXXXXXXX\n
2. Open ranges and fill with the amount of times to search before and after in the number of days, hours, minutes and seconds. Format of each line:dddd:hh:mm:ss dddd:hh:mm:ss
3. Run search_many_times.py

The graceDB event names will be stored in data/ in the folders of the names and time ranges before and after. Format for each file: gpsXXXXXXXXXX-XdXhXmXs

