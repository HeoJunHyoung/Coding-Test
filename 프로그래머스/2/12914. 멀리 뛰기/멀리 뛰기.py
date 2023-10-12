def solution(n):
    
    jump = [0]*(n+1)
    
    jump[0] = 1
    jump[1] = 2
    
    for i in range(2, n):
        jump[i] = jump[i-2] + jump[i-1]
    
    return jump[n-1]%1234567