# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import date
# import calendar
# from calendar import HTMLCalendar

# def index(request, year=None, month=None):
#     if year is None or month is None:
#         today = date.today()
#         year = today.year
#         month = today.month
#     else:
#         year = int(year)
#         month = int(month)

#     # Validate year and month
#     if year < 1900 or year > 2099:
#         year = date.today().year
#     if month < 1 or month > 12:
#         month = date.today().month

#     # Get month name and format the calendar
#     month_name = calendar.month_name[month]
#     title = f"MyClub Event Calendar - {month_name} {year}"
#     cal = HTMLCalendar().formatmonth(year, month)

#     # Return the formatted HTML response with the calendar
#     return HttpResponse(f"<h1>{title}</h1><p>{cal}</p>")


from django.shortcuts import render
from datetime import date
import calendar
from calendar import HTMLCalendar

def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099:
        year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    return render(request, 'base.html', {'title': title, 'cal': cal})
