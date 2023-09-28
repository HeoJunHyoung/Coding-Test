def solution(arr):
    
    index1 = 0
    index2 = 0
    
    for i in range(0, len(arr)):
        if arr[i]==2:
            index1 = i
            break
    
    for i in range(len(arr)-1, 0, -1):
        if arr[i]==2:
            index2 = i
            break
    
    if index1==0 and index2 ==0:
        return [-1]
    else:
        return arr[index1:index2+1]