def solution(my_string):
    
    my_string = my_string.lower()
    newString = sorted(my_string)
    return ''.join(newString)