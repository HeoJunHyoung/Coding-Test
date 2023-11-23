def solution(n):
    
    s, e = 1, 1
    count = 1
    total = 1
    
    while e != n:
        if total == n:
            count += 1
            total -= s
            s += 1
            
        elif total < n:
            e += 1
            total += e
        else:
            total -= s
            s += 1
            
    return count