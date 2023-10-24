import copy

def solution(triangle):
    n = len(triangle)
    m = len(triangle[-1])
    
    A = [[0 for _ in range(n)] for _ in range(m)]
    #print(A)
    
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            A[i][j] = triangle[i][j]
            
    D = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(n):
        D[i][0] = D[i-1][0] + A[i][0]
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            D[i][j] = max(D[i-1][j-1], D[i-1][j]) + A[i][j]
    
    return max(D[n-1])
    
    