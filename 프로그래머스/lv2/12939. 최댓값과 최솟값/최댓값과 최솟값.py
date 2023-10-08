def solution(s):
    s = s.split(' ')
    s = list(map(int, s))
    maxim, minim = max(s), min(s)
    return str(minim)+' '+str(maxim)