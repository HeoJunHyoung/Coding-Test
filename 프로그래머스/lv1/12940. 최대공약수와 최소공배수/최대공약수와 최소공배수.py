def solution(n, m):
    
    result = []
    
    large = max(n, m)
    small = min(n, m)
    
    
    # 최대공약수
    start = 1
    value1 = 0
    while start <= small:
        if large%start ==0 and small%start == 0:
            value1 = start
        start += 1
    #print(value1)
    
    value2 = 0
    # 최소공배수
    if large%small==0:
        value2 = large
    else:
        value2 = small*large//value1
    #print(value2)
    
    return [value1, value2]
    
    
    
    
