def solution(my_strings, parts):
    answer = ''
    index1 = 0
    index2 = 0
    
    for i in range(0, len(my_strings)):
        index1 = parts[i][0]
        index2 = parts[i][1]
        
        answer += my_strings[i][index1:index2+1]
    
    
    
    return answer