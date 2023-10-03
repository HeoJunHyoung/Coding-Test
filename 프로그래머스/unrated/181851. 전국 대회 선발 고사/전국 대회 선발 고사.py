def solution(rank, attendance):
    
    newList = []
    
    for i in range(1, len(rank)+1):
        if attendance[rank.index(i)] == True: # rank.index(i) = 6
            newList.append(rank.index(i))
            
    print(newList)
    return 10000*newList[0] + 100*newList[1] + newList[2]