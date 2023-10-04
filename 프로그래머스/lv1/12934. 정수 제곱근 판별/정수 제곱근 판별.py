def solution(n):
    
    start = 1
    while start*start < n:
        start+=1
    return (start+1)*(start+1) if start*start==n else -1