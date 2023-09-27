def solution(my_string):
    answer = ''
    
    for i in range(0, len(my_string)):
        if my_string[i] < 'a':
            answer += my_string[i].lower()
        else:
            answer += my_string[i].upper()
    
    
    return answer