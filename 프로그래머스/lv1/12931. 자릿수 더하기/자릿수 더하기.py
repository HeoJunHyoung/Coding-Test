def solution(n):
    
    n = str(n)
    
    return sum([int(n[i]) for i in range(0, len(n))])