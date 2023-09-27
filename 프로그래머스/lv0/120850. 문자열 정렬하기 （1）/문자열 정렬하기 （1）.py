def solution(my_string):
    answer = []
    
    for i in range(0, len(my_string)):
        if my_string[i] < 'a':
            answer.append(my_string[i])
    
    return list(map(int, sorted(answer)))