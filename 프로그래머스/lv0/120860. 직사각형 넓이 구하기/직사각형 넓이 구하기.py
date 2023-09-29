def solution(dots):
    
    xList = []
    yList = []
    
    for i in range(0, len(dots)):
        xList.append(dots[i][0])
        yList.append(dots[i][1])
    
    return (max(xList)-min(xList)) * (max(yList)-min(yList))