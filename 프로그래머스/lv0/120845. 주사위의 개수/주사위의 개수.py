def solution(box, n):
    
    newList = [i//n for i in box]
    
    result = 1
    
    for i in newList:
        result = result * i
        
    return result