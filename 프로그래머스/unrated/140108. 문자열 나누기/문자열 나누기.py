def solution(s):
    
    cnt1 = 0
    cnt2 = 0
    result = 0
    
    for i in s:
        if cnt1 == cnt2:
            result += 1
            criterion = i
        if i == criterion:
            cnt1 += 1
        else:
            cnt2 += 1
    
    return result
            