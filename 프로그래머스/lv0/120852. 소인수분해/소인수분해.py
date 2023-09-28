def solution(n):
    
    div_num = 2
    num_set = set()
    
    while n > 1:      # n = 420
        
        if n % div_num != 0: 
            div_num += 1
        else:
            num_set.add(div_num) # {2}
            n = n / div_num # n = 210
    
    return sorted(list(num_set))
    
    
    
        