def serch_index(slist,sint):
    resultIndex = []
    if sint in slist:
        for i in range(len(slist)):
            if slist[i] == sint:
                resultIndex.append(i)

    return resultIndex
    


print(serch_index([35,28,30,29,30],30))
print(serch_index([35,28,30,29,30],31))
