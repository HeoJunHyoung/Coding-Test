def solution(n, numlist):
    
    return [numlist[i] for i in range(0, len(numlist)) if numlist[i]%n==0]