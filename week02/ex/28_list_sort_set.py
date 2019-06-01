def list_sort_set(a):
    a = list(set([int(x) for x in a]))
    a.sort()
    return a
