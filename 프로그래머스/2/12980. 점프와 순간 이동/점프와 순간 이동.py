def solution(n):
    
    count = 0
    N = n
    mok = n
    
    if N % 2 != 0:
        count += 1
    #print(count)
    while mok != 1:
        
        mok = mok // 2
        na = mok % 2
        if na == 1:
            count += 1
        #print(count)
    
    return count