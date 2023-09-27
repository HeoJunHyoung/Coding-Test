def solution(my_string):
    answer = ''
    
    return ''.join([my_string[i].lower() if my_string[i] < 'a' else my_string[i].upper() for i in range(0, len(my_string))])