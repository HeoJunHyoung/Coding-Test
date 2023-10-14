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
    
    # 뒤에 0 붙이기
    #if jisoo != 0:
        #for i in range(jisoo):
            #answer += '0'
    
    lenStr = len(answer)
    
    answer = str(int(answer[::-1]))
    #print(answer)
    
    result = 1
    
    for i in range(lenStr): # 0 1 2 3 4
        result = result + int(answer[i])*(3**(lenStr-i-1))
    
    return result - 1
    
    
    
    
    
    
    
    
        