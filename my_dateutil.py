import dateutil
import datetime
from dateutil.relativedelta import relativedelta

#日付の計算。years, months, weeks, days, hours, minutes, seconds, microsecondsの加算・減算が可能。
today = datetime.date.today()
print(today)
print(today + relativedelta(months=+1))
# + relativedelta(month=+a, weeks=-b)のように複数要素に加減算が可能。
# "+"をつけずに記述するとただの代入になる。