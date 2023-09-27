def solution(intStrs, k, s, l):
    
    listA = []
    
    for i in range(0, len(intStrs)):
        listA.append(intStrs[i][s:s+l])
    
    
    return [int(i) for i in listA if int(i) > k]