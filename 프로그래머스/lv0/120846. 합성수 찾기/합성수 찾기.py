def solution(n):
    
    yaksu = 0
    total = 0
    
    for i in range(4, n+1):
        yaksu = 0
        
        for j in range(1, i+1):
            if i%j==0:
                yaksu += 1
        if yaksu >=3 :
            print(i)
            total += 1
    
    return total