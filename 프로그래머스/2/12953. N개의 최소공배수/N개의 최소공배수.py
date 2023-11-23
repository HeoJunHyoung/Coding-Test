from collections import deque
def gcd(n1, n2):
    if n2 < n1 :
        n1, n2 = n2, n1
    
    while n1%n2 != 0:
        n1, n2 = n2, n1%n2
    
    return n2

def lcm(n1, n2):
    return n1*n2 // gcd(n1, n2)

def solution(arr):
    dq = deque(arr)
    x = lcm(dq.popleft(), dq.popleft())
    while dq:
        x = lcm(x, dq.pop())
    return x
    