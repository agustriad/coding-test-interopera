from datetime import datetime, timezone, timedelta

def current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_date(timestamp):
    date_fromtimestamp = datetime.fromtimestamp(timestamp)

    today = datetime.today().date()
    if date_fromtimestamp.date() == today:
        return "Today"
    elif date_fromtimestamp.date() == (today - timedelta(days=1)):
        return "Yesterday"
    elif date_fromtimestamp.date() >= (today - timedelta(days=7)):
        return  "Previous 7 Days"
    else:
        return date_fromtimestamp.strftime("%Y-%m-%d")

