def solution(n):
    
    
    result = 0
    
    if n%2 != 0:
        result = sum([i for i in range(1, n+1) if i%2!=0])
    else:
        result = sum([i*i for i in range(1, n+1) if i%2==0])
    return result