from datetime import datetime

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def toDateTime(date):
    if not date:
        return None
    return datetime.strptime(date, TIME_FORMAT)