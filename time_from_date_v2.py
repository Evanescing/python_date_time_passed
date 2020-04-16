import datetime
from dateutil import relativedelta


fromDate = '10.04.2020'
fromDate = datetime.datetime.strptime(fromDate, '%d.%m.%Y')
todayDate = datetime.datetime.now()
diff = relativedelta.relativedelta(todayDate, fromDate)
print('Was passed {} years, {} months and {} days'.format(diff.years, diff.months, diff.days))
