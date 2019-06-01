def dict_count(a):
    occur = {}
    for item in a:
        if item in occur:
            occur[item] += 1
        else:
            occur[item] = 1
    return dict(occur)
