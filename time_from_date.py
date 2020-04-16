import calendar
import datetime


textDate = '10.04.2020'
arDate = textDate.split('.')
nowDate = datetime.date.today()
years = int(nowDate.year) - int(arDate[2])
if int(nowDate.month) >= int(arDate[1]):
  monthes = int(nowDate.month) - int(arDate[1])
else:
  years = years - 1
  monthes = int(nowDate.month) + 12 - int(arDate[1])
if int(nowDate.day) >= int(arDate[0]):
  days = int(nowDate.day) - int(arDate[0])
else:
  monthes = monthes - 1
  daysInMonth = calendar.monthrange(int(arDate[2]), int(arDate[1]))[1]
  days = int(nowDate.day) + daysInMonth - int(arDate[0])

print('From 10.04.2020 was passed {} Years, {} Monthes and {} Days.'.format(years, monthes, days))
