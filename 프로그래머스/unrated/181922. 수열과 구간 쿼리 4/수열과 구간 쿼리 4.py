def solution(arr, queries):
    
    for querie in queries:
        for increase in range(querie[0], querie[1]+1):
            if increase % querie[2] == 0:
                arr[increase] += 1
        
    return arr
    
    
    