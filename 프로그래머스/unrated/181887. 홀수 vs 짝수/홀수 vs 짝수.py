def solution(num_list):
    
    evenList = [num_list[i] for i in range(0, len(num_list), 2)]
    oddList = [num_list[i] for i in range(1, len(num_list), 2)]
    
    evenSum = 0
    oddSum = 0
    
    for i in range(0, len(evenList)):
        evenSum += evenList[i]
                   
    for i in range(0, len(oddList)):
        oddSum += oddList[i]
                   
    if evenSum > oddSum:
        return evenSum
    elif evenSum < oddSum:
        return oddSum
    else:
        return evenSum