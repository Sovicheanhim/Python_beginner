def current_time():
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%H:%M:%S")
