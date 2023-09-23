def solution(num_list):
    
    
    if len(num_list)>=11:
        result = 0
        for i in num_list:
            result += i
    else:
        result = 1
        for i in num_list:
            result *= i
    
    return result
        