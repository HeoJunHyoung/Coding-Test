def solution(n):
    
    increase = 1
    count = 0
    temp = 0
    
    while count < n:
        temp = increase
        if '3' in str(increase) or increase%3==0:
            increase += 1
        else:
            increase += 1
            count += 1
        
    
    return temp
    
    
    