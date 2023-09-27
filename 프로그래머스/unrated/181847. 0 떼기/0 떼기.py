def solution(n_str):
    answer = ''
    i=0
    
    while n_str[i] == '0':
        i += 1
    
    for j in range(i, len(n_str)):
        answer += n_str[j]
    
    return answer