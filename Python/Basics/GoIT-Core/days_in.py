from datetime import date

def get_days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29  # February in a leap year
        else:
            return 28  # February in a non-leap year
    else:
        return "Month must be in 1..12"

# Test the function
print(get_days_in_month(2, 2020))  # Outputs: 29
print(get_days_in_month(2, 2021))  # Outputs: 28
