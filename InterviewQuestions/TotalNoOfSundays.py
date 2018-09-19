

# For the years 1901 to 2000, count the total number of Sundays that fell on the first of a month.
# steps:
#       1) Take start year
#       2) Take end year
#       3) use datetime to get sinday
#       4) loop throough years and count all sundays

import datetime 


#print(timedelta(days=365, hours=8, minutes=15))


startyear=1900
endyear=2000

c=0
for y in range(startyear, endyear +1):
    for m in range(1,13):
        
        d=datetime.datetime(y,m,1)
      
        if d.weekday()==6:
            c += 1
print(c)
            
                