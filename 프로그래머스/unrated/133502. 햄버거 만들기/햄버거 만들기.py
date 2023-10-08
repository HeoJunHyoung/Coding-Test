def solution(ingredient):
    result = 0
    temp = []
    
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1, 2, 3, 1]:
            result += 1
            del temp[-4:]
            
    return result