def solution(n):
    result = 0
    summ = 0
    for i in range(1,n+1): # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        summ=0
        for j in range(i, n+1): # 
            summ = summ + j
            if summ == n:
                print(i, j)
                result += 1
            elif summ > n:
                break
            
            
    
    return result