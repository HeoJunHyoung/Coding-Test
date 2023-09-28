def solution(s):
    newList = []
    
    s = s.split(' ')
    
    for i in range(0, len(s)):
        if s[i] != 'Z':
            newList.append(s[i])
        else:
            newList.pop()
    
    
    return sum([int(i) for i in newList])