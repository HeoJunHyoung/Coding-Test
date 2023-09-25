def solution(my_string, m, c):
    answer = ''
    start_point = c - 1
    
    for i in range(0, len(my_string)//m):
        answer += my_string[start_point + m*i]
        
    return answer