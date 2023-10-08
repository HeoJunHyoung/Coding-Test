def solution(dartResult):
    
    splitedResult = dartResult[:]
    answer = 0
    
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            splitedResult = splitedResult.replace(dartResult[i], dartResult[i]+' ')
        elif dartResult[i] == '*':
            splitedResult = splitedResult.replace(dartResult[i], '* ')
        elif dartResult[i] == '#':
            splitedResult = splitedResult.replace(dartResult[i], '# ')
        else:
            continue
            
    
    splitedResult = splitedResult.split(' ')
    result = []
    newList = [splitedResult[i] for i in range(len(splitedResult)) if splitedResult[i] != '']
    print(newList)
    
    for i in range(len(newList)):
        if newList[i][-1] == 'S':
            result.append(int(newList[i][:-1]))
        elif newList[i][-1] == 'D':
            result.append(int(newList[i][:-1])**2)
        elif newList[i][-1] == 'T':
            result.append(int(newList[i][:-1])**3)
            
        elif newList[i][-1] == '*':
            if len(result)==1:
                result[0] = result[0]*2
            elif len(result)==2:
                result[0] = result[0]*2
                result[1] = result[1]*2
            else:
                result[1] = result[1]*2
                result[2] = result[2]*2
                
        elif newList[i][-1] == '#':
            result[-1] = result[-1]*(-1)
                
    return sum(result)
            
    
    
    
    
    
    
    
    