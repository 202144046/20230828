def merge_list(list_1, list_2):
    result = [ d for d in list_2 if d not in list_1 ]
    for i in range(len(result)):
        
        list_1.append(result[i])
    list_1.sort()
    return list_1

print(merge_list([1,2,3,4],[1,2,5]))

print(merge_list([0,1,10],[1,2,6,7,8]))

