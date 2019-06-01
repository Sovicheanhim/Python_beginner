def current_date():
    from datetime import date
    today = date.today()
    return today.strftime("%Y-%m-%d")
