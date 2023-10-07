def solution(strings, n):
    
    newList = [[] for i in range(0, len(strings))]
    
    for i in range(0, len(strings)):
        newList[i].append(strings[i][n])
        newList[i].append(strings[i])
        
    sorted_newList = sorted(newList)
    print(sorted_newList)
    
    return [sorted_newList[i][1] for i in range(0, len(newList))]