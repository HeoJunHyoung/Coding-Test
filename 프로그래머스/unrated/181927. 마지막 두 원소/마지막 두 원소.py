def solution(num_list):
    
    last_elem = num_list[-1]
    prev_elem = num_list[-2]
    
    if last_elem>prev_elem:
        num_list.append(last_elem-prev_elem)
    else:
        num_list.append(last_elem*2)
    
    return num_list