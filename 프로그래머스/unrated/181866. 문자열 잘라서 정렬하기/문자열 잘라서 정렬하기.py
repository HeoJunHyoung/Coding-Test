def solution(myString):
    answer = []
    
    myString = myString.split('x')
    
    for i in range(0, len(myString)):
        if myString[i] != '':
            answer.append(myString[i])
    
    
    return sorted(answer)