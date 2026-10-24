from datetime import datetime

def get_str_date(date):
    dt = datetime.strptime(date,"%Y-%m-%d %H:%M:%S.%fZ")
    return dt.strftime("%A %d %B %Y")

date='2021-05-27 17:08:34.149Z'
print(get_str_date(date))