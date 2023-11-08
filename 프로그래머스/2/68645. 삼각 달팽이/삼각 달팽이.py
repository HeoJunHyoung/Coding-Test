def solution(n):
    
    inc = 1
    row, col = -1, 0
    triangle = [[0 for _ in range(n)] for _ in range(n)]
    result = []
    #print(triangle)
    
    for i in range(n): # 0 1 2 3
        for j in range(i, n): # 0 1 2 3
            
            if i % 3 == 0:
                row += 1
            
            elif i % 3 == 1:
                col += 1
            
            else: 
                row -= 1
                col -= 1
            
                
            triangle[row][col] = inc
            inc += 1
        
    for i in range(len(triangle)):
        for j in range(i+1):
            result.append(triangle[i][j])
    
    return result
                