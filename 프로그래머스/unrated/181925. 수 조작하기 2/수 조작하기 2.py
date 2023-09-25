def solution(numLog):
    answer = ''
    
    
    for i in range(1, len(numLog)):
        result = numLog[i] - numLog[i-1]
        
        if result == 1:
            answer = answer + 'w'
        elif result == -1:
            answer = answer + 's'
        elif result == 10:
            answer = answer + 'd'
        else:
            answer = answer + 'a'
    
    
    return answer