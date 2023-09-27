def solution(my_string, is_prefix):
    
    all_string = []
    
    for i in range(0, len(my_string)):
        all_string.append(my_string[0:i+1])
    
    for i in all_string:
        if is_prefix == i:
            return 1
    return 0