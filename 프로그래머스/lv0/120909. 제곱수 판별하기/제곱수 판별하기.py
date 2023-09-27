def solution(n):
    answer = 0
    accum = 0
    start = 2
    
    while accum <= n:
        if accum == n:
            return 1
        accum = start * start
        start += 1
    
    return 2