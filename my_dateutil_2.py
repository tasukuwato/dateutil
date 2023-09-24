import dateutil
import datetime
#timezoneを扱うために「pytz」をimportする
import pytz
from dateutil import tz


u = dateutil.tz.tzutc()
print(datetime.datetime.now(u))

#timezoneの処理
u = dateutil.tz.gettz('JP/Japan')
#timezoneはwikipediaを参照:https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
print(datetime.datetime.now(u))