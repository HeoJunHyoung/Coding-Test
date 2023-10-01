def solution(sides):
    
    minNum = min(sides)
    maxNum = max(sides)
    
    count = 0
    x1 = maxNum
    
    while minNum+x1>maxNum and x1<=maxNum:
        x1 -= 1
        count += 1
    
    x2 = maxNum+1
    while minNum+maxNum>x2:
        x2 += 1
        count += 1
        
    return count
        
        