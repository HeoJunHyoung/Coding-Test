def solution(arr, k):
    
    result = []
    
    for i in range(0, len(arr)):
        if arr[i] not in result:
            result.append(arr[i])
        if len(result) == k:
            break
    
    if len(result) < k:
        for i in range(0, k-len(result)):
            result.append(-1)
            
    return result
        