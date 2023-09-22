def solution(n):
    listSum = [i for i in range(0,n+1) if i%2==0] # 0, 1, 2, 3, 4
    sum = 0
    for i in listSum:
        sum += i
        
    return sum