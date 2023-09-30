def solution(arr):
    
    upperNumber = 1
    
    while len(arr) >= (2**upperNumber):
        upperNumber += 1
    
    addIndex = 2**upperNumber - len(arr)
    
    if addIndex == len(arr):
        return arr
    else:
        for i in range(0, addIndex):
            arr.append(0)
        return arr