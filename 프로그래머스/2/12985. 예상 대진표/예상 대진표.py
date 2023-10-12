def solution(n,a,b):
    
    count = 0
    
    while a != b:
        count += 1
        
        if a%2 != 0:
            a += 1
        if b%2 != 0:
            b += 1
        a = a // 2
        b = b // 2
    
    return count