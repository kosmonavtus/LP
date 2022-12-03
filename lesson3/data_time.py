from datetime import datetime, timedelta

dt_now = datetime.now()



print(dt_now - timedelta(days=1))
print(dt_now)
print(dt_now - timedelta(days=30))

data_string =  '01/01/25 12:10:03.234567'
date_from_str = datetime.strptime(data_string, '%d/%m/%y %H:%M:%S.%f') 
print(date_from_str)

