def solution(names):
    
    term = 5
    
    return [names[i] for i in range(0, len(names)) if i%5==0]