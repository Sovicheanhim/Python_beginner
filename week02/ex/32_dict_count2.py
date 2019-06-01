def dict_count2(a):
        if a == []:
            return "Your string is empty."
        else:
            li = dict()
            sum = 0
            for item in a:
                li[item] = a.count(item)
                sum += 1
            print("TOTAL: "+str(sum))
            return sorted(li.items(), key=lambda x: (x[0], x[1]))
