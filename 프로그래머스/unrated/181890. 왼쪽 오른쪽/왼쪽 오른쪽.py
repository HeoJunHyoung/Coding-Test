def solution(str_list):
    answer = []
    
    for i in range(0, len(str_list)):
        if str_list[i] == 'l':
            return (str_list[0:i])
        elif str_list[i] == 'r':
            return (str_list[i+1:len(str_list)])
        
    return answer