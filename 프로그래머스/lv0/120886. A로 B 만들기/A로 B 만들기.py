def solution(before, after):

    total = 0
    
    for i in range(len(before)):
        if after.count(before[i]) != before.count(before[i]):
            return 0
    
    return 1