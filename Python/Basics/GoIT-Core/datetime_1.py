from datetime import datetime


def get_days_from_today(date):
    a=date.split('-')
    d1=datetime.now().date()
    d2=datetime(year=int(a[0]),month=int(a[1]),day=int(a[2])).date()
    delta=d1-d2

    return delta.days



date='2021-10-09'
print(get_days_from_today(date))



