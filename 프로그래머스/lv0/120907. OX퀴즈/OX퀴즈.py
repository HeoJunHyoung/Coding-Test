def solution(quiz):
    answer = []
    
    for i in range(0, len(quiz)):
        quiz[i] = quiz[i].split(' ')
    
    
    # print(quiz)
    
    for i in range(0, len(quiz)):
        
        if quiz[i][1] == '-':
            result = int(quiz[i][0]) - int(quiz[i][2])
        else:
            result = int(quiz[i][0]) + int(quiz[i][2])
        
        if result == int(quiz[i][-1]):
            answer.append('O')
        else:
            answer.append('X')
    
    return answer