def solution(arr):
    
    newList = []
    
    for i in range(0, len(arr)):
        for j in range(0, arr[i]):
            newList.append(arr[i])
            
    return newList