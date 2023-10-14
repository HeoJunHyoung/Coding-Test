def findStart(n):
    jisoo = 0
    
    while True:
        cur = 3**jisoo
        nex = 3**(jisoo+1)
        if cur<=n and nex>n:
            return jisoo
        jisoo += 1 
            
def solution(n): 
    
    answer = ''
    jisoo = findStart(n) # 3
      
    #print(jisoo)   
    
    while n != 0:
        if n % (3**jisoo) == 0:
                result = n // (3**jisoo)
                answer += str(result)
                break
        else:
            temp = n//(3**jisoo)
            n = n - (temp) * (3**jisoo)
            answer += str(temp)
        jisoo -= 1
    
    answer = str(int(answer[::-1]))
    
    result = 1
    for i in range(len(answer)): # 0 1 2 3 4
        result = result + int(answer[i])*(3**(len(answer)-i-1))
    
    return result - 1
    
    
    
    
    
    
    
    
        