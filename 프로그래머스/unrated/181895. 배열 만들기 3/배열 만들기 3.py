def solution(arr, intervals):
    answer = []
    newList = []
    
    answer.append(arr[intervals[0][0]:intervals[0][1]+1])
    answer.append(arr[intervals[1][0]:intervals[1][1]+1])
    
    for element in answer:
        newList += element
    
    return newList