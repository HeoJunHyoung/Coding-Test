def solution(num_list):
    
    div_count = 0
    
    for i in range(len(num_list)):
        number = num_list[i]
        local_count = 0
        while number != 1:
            
            if number % 2 == 0:
                number = number / 2
                local_count += 1
            else:
                number = number -1
                number = number /2
                local_count += 1
        div_count += local_count
    
    return div_count
            
            