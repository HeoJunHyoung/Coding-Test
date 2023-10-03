def solution(n):
    
    start = 1
    result = 0
    
    while start<=n:
        if n%start==0:
            result += start
        start+=1
    
    return result