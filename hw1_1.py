from datetime import datetime
from collections import defaultdict 


def get_birthdays_per_week(users):
    today=datetime.today().date() 
    birthdays_per_week = defaultdict(list)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date() 
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_next_year = birthday.replace(year=today.year+1)
        else:
            delta_days = (birthday_this_year - today).days
            if delta_days<7:
                birthday_weekday = birthday_this_year.strftime('%A')
                if birthday_weekday=='Sunday' or birthday_weekday=='Saturday':
                    birthday_weekday='Monday'
                    birthdays_per_week[birthday_weekday].append(name)
                else:
                    birthdays_per_week[birthday_weekday].append(name)

    birthday_next_week=sorted(birthdays_per_week.items())
    for i in birthday_next_week:
        print(i[0],':',', '.join(i[1]))



