import datetime

date_offset = 0

def get_date():
        date = datetime.datetime.now() + datetime.timedelta(days=date_offset)
        day_of_week = date.weekday()
        date_for_url = format_date_for_url(date)
        return(date_for_url)

def format_date_for_url(date):
        month = date.strftime("%m")
        day = date.strftime("%d")
        year = date.strftime("%Y")
        date_for_url = month +"%2f"+day+"%2f"+year
        return(date_for_url)

def get_day_of_week():
        date = datetime.datetime.now() + datetime.timedelta(days=date_offset)
        day_of_week = date.weekday()
        return(day_of_week)