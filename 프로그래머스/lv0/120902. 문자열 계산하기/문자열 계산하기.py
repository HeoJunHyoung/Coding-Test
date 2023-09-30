def solution(my_string):
    
    
    my_string = my_string.split(' ')
    result = int(my_string[0])
    num_list = []
    op_list = []
    
    for i in range(1, len(my_string)):
        if my_string[i].isdigit():
            num_list.append(my_string[i])
        else:
            op_list.append(my_string[i])
    
    
    for i in range(0, len(op_list)):
        if op_list[i] == '+':
            result += int(num_list[i])
        else:
            result -= int(num_list[i])
    
    return result
    