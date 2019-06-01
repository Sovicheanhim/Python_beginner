def timestamp_to_str(a):
    from datetime import datetime
    try:
        a = int(a)
        timestamp = datetime.utcfromtimestamp(a)
        return timestamp
    except TypeError:
        print("Your timestamp is not valid.")
        return 0
    except ValueError:
        print("Your timestamp is not valid.")
        return 0
