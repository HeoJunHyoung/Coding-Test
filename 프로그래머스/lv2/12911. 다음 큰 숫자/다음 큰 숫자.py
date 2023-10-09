def solution(n):
    answer = 0
    n_one = bin(n).count('1')
    
    while(1):
        n = n + 1
        if n_one == bin(n).count('1'):
            break
            
    return n