def time_list(a):
    import time
    from datetime import datetime
    time_sleep = []
    try:
        a = int(a)
        if a > 0:
            for second in range(0,a):
                now = datetime.now()
                time_sleep.append(now.strftime("%H:%M:%S"))
                time.sleep(1)
            return time_sleep
        else:
            print("Invalid integer.")
            return time_sleep
    except TypeError:
        print("Invalid integer.")
        return time_sleep
    except ValueError:
        print("Invalid integer.")
        return time_sleep
