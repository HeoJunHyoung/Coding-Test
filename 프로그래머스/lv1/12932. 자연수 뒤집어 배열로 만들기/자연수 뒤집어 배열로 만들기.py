def solution(n):
    n=str(n)
    n = n[len(n)::-1]
    return [int(n[i]) for i in range(0, len(n))]
    