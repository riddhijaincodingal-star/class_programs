import calendar
from pprint import pprint


year=int(input("enter year"))
month=int(input("enter month"))

print(calendar.month(year,month))  #pass arguments year and month


for month in range(1,13):
    
  pprint(calendar.month_name[month])
  
print(calendar.Calendar().iterweekdays(year))  