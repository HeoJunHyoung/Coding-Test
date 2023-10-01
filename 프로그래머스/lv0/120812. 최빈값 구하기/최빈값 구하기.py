def solution(array):
    
    freqList = [0]*1000
    
    for i in array:
        freqList[i] += 1
    if freqList.count(max(freqList)) >= 2:
        return -1
    else:
        return freqList.index(max(freqList))
    