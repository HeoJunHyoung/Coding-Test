def solution(my_string):
    
    sum = 0
    my_string = list(my_string)
    listA = ['1','2','3','4','5','6','7','8','9','0']
    newList = []
    
    for i in range(0, len(my_string)):
        for j in range(0, len(listA)):
            if my_string[i] == listA[j]:
                sum += int(my_string[i])
    
    return sum