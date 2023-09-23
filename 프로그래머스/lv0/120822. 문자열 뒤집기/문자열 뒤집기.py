def solution(my_string):
    
    # return my_string[::-1]
    
    my_string = list(my_string)
    my_string.reverse()
    return ''.join(my_string)
    