def solution(n):
    
    
    
    array = []
    for i in range(0, n):
        array.append([])
        for j in range(0, n):
            array[i].append(0)
    
    
    
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if i==j:
                array[i][j] = 1
                
    return array