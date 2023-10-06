def solution(d, budget):
    
    d = sorted(d)
    count = 0
    
    if d[0]>budget:
        return 0
    
    for i in d:
        if budget - i >= 0:
            budget = budget - i
            count += 1
    
    return count
    
    
        



