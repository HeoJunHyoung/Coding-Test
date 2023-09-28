def solution(my_string, s, e):
    
    answer = ''
    if s != 0:
        my_string = my_string[0:s] + my_string[e:s-1:-1] + my_string[e+1:len(my_string)]
    else:
        my_string = my_string[e:s:-1] + my_string[0] + my_string[e+1:len(my_string)]
    
    return my_string