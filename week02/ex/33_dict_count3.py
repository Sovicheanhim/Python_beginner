def dict_count3(a):
    if a == []:
        return "Your string is empty."
    else:
        li = dict()
        sum = 0
        for item in a:
            li[item] = a.count(item)
            sum += 1
        print("TOTAL: " + str(sum))
        return sorted(li.items())


# print(dict_count3(['a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'e', 'e', 'e']))