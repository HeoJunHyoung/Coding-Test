def solution(s):
    
    if s[0] == '-':
        s = s[1:]
        return int(s)*-1
        
    return int(s)