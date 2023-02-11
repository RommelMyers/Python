from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)
now = now + relativedelta(months=10, weeks=1, hour=13)
print(now)