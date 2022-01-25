import datetime
import dateutil.tz

central = dateutil.tz.gettz('US/Central')

def get_date(day_offset):
    #day_offset = day_offset
    date = datetime.datetime.now(tz=central) + datetime.timedelta(days=day_offset)
    day_of_week = date.weekday()
    date_for_url = format_date_for_url(date)
    return(date_for_url)

def format_date_for_url(date):
    month = date.strftime("%m")
    day = date.strftime("%d")
    year = date.strftime("%Y")
    date_for_url = month +"%2f"+day+"%2f"+year
    return(date_for_url)

def get_day_of_week(day_offset):
    date = datetime.datetime.now(tz=central) + datetime.timedelta(days=day_offset)
    day_of_week = date.weekday()
    return(day_of_week)