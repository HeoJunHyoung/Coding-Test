def solution(arr):
    
    min_value = min(arr)
    del arr[arr.index(min_value)]
    return arr if arr else [-1]