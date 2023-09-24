def solution(order):
    
    
    listGame = ['3','6','9']
    order = list(str(order))
    result = 0
    for i in order:
        for j in listGame:
            if i==j:
                result += 1
                
    return result