## 1. 진수 변환 함수 ##
def convert(n, q):
    result = ''
    
    while n>0:
        n, mod = divmod(n, q)
        result += str(mod)
    
    return result[::-1]

## 2. 소수 판별 함수 ## 
def isPrime(n): 
    if n<2:
        return False
    for i in range(2, int(n**(1/2)+1) ):
        if n%i==0:
            return False
    return True
    
## 3. 메인 함수 ##
def solution(n, k):
    
    n = convert(n, k)
    answer = 0
        
    if len(n)==1 and isPrime(n):
        return 1
    
    listX = n.split('0')
    
    for X in listX:
        if X == '':
            continue
        if isPrime(int(X)):
            answer += 1
    
    return answer
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    