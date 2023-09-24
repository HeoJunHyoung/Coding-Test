def solution(array):
    
    sortedArray = sorted(array)
    return [sortedArray[-1],array.index(max(sortedArray))]