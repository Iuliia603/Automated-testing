from datetime import datetime
import calendar


def get_day_of_week(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        day_number = date.weekday()
        day_name = calendar.day_name[day_number]
        return day_name
    except ValueError:
        return "Incorrect date format"

user_date = input("Enter the date in the format 'YYYY-MM-DD': ")

day_of_week = get_day_of_week(user_date)
print("Date: {}, day of the week: {}".format(user_date, day_of_week))