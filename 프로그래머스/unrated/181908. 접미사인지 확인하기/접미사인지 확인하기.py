def solution(my_string, is_suffix):
    
    all_string = []
    
    for i in range(0, len(my_string)):
        all_string.append(my_string[i:len(my_string)])
    
    for i in all_string:
        if is_suffix == i:
            return 1
    return 0
    