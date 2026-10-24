from datetime import date


def get_days_in_month(month, year):
    if month < 1 or month > 12:
        return "Некоректний номер місяця"
    
    if month == 12:
        days = date(year + 1, 1, 1) - date(year, month, 1)
    else:
        days = date(year, month + 1, 1) - date(year, month, 1)
    
    return days.days
        
    