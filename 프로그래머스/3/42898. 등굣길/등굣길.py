def solution(m, n, puddles):
    
    D = [[0 for _ in range(m+1)] for _ in range(n+1)]
    D[1][0] = 1
    
    for x, y in puddles:
        D[y][x] = -1
    
    for i in range(1, len(D)):
        for j in range(1, len(D[i])):
            if D[i][j] == -1:
                continue
            else:
                up = D[i-1][j]
                left = D[i][j-1]
                if up == -1:
                    up = 0
                if left == -1:
                    left = 0
                D[i][j] = up + left
    
    return (D[-1][-1])%1000000007
