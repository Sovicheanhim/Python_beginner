def list_sort_int(a):
    x = [int(x) for x in list(set(a)) if x.isdigit()]
    x.sort()
    return x
