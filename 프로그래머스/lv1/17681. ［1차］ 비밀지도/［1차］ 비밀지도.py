def solution(n, arr1, arr2):
    
    result1 = []
    result2 = []
    result = []
    temp = ''
    
    for i in range(n):
        row1 = ''
        jisoo1 = n-1
        row2 = ''
        jisoo2 = n-1
        for j in range(n):
            
            if arr1[i]//(2**jisoo1) == 0:
                row1 += '0'
                jisoo1 -=1
            else:
                arr1[i] = arr1[i]%(2**jisoo1)
                row1 += '1'
                jisoo1 -= 1
                
            if arr2[i]//(2**jisoo2) == 0:
                row2 += '0'
                jisoo2 -=1
            else:
                arr2[i] = arr2[i]%(2**jisoo2)
                row2 += '1'
                jisoo2 -= 1
                
        result1.append(row1)
        result2.append(row2)
    
    for i in range(n):
        temp = ''
        for j in range(n):
            temp += '#' if int(result1[i][j]) or int(result2[i][j]) else ' '
        result.append(temp)    
    
    return result
    
    
    
    
    
    
    
    