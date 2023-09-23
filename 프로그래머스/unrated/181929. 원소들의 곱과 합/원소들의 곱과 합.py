def solution(num_list):
    
    multi = 1
    sum = 0
    
    for i in num_list:
        multi *= i
        sum += i
    
    sum = sum * sum
    if multi > sum:
        return 0
    else:
        return 1