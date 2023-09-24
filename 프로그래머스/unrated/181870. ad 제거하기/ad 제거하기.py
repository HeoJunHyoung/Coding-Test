def solution(strArr):
    
    newList = []
    
    for i in range(0, len(strArr)):
        if "ad" not in strArr[i]:
            newList.append(strArr[i])
            
    return newList