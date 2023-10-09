def solution(n):
    
    f = [0, 1]
    for i in range(2, n+1): # 2 3 4 5
        f.append(f[-2]+f[-1])
        #print(f)
    
    return f[n]%1234567