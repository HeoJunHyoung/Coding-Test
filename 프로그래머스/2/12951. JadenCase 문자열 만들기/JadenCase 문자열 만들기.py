def solution(s):
    s = s.lower()
    answer = ''
    
    list_string = s.split(' ')
    print(list_string)
    
    for string in list_string:
        if string =='':
            answer += ' '
        elif string[0].isalpha():
            answer += string[0].upper()+string[1:] + ' '
        else:
            answer += string + ' '
    
    return answer[:-1]