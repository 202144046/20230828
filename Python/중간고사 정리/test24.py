def add_list(alist,blist):

    maxlen = max(len(alist),len(blist))

    alist += [0] * (maxlen - len(alist))
    blist += [0] * (maxlen - len(blist))

    result = [alist[i] + blist[i] for i in range (maxlen)]

    return result


print(add_list([1,2,3,4],[1,2]))

print(add_list([0,1],[1,2,6,7,8]))
