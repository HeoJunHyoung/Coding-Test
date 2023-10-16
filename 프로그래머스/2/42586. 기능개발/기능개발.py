def solution(progresses, speeds):
    
    index = 0
    count = 0
    result = []
    
    while index < len(progresses):
        count = 0
        flag = False
        
        while progresses[index] >= 100:
            index += 1
            count += 1
            flag = True
            if index == len(progresses):
                break
            
        
        if flag == True:
            result.append(count)
        
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
    
    return result
    
    
            
            