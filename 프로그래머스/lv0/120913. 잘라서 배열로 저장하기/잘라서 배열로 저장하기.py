def solution(my_str, n):
    answer = []
    
    
    div_num = len(my_str)//n + 1 if len(my_str)%n!=0 else len(my_str)//n
    
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
        
    return answer