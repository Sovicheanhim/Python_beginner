def list_sort_str(a):
    x = [x for x in list(set(a)) if not x.isdigit() ]
    x.sort()
    return x
