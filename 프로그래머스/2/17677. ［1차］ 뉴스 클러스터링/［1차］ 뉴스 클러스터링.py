def solution(str1, str2):
    
    A = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    B = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    print(A)
    print(B)
    if not A and not B:
        return 65536
    
    
    
    setA = list(set(A))
    setB = list(set(B))
    
    gyo, hap = 0, 0
    
    print(setA)
    print(setB)
    
    for x in setA:
        if x in A and x in B:
            gyo += min(A.count(x), B.count(x))
    #print(gyo)
    
    for x in list(set(setA+setB)):
        hap += max(A.count(x), B.count(x))
    #print(hap)
    
    return int(gyo/hap*65536)