def solution(arr, queries):
    
    for i in range(len(queries)):
        startNum = queries[i][0]
        endNum = queries[i][1] + 1
        for j in range(startNum, endNum):
            arr[j] += 1
    
    return arr