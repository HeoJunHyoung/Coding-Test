def solution(my_string):
    
    mo = ['a','i','o','u','e']
    answer = ''
    
    
    for i in range(0, len(my_string)):
        if my_string[i] not in mo:
            answer += my_string[i]
            
    return answer