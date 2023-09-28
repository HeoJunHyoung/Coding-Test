def solution(array):
    
    newArray = ''
    for i in array:
        newArray += str(i)
    
    return newArray.count('7')