def solution(arr1, arr2):
    
    result = [[] for i in range(0,len(arr1))]
    # print(result)
    
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1[i])):
            result[i].append(arr1[i][j]+arr2[i][j])
        
    return result