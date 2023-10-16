def solution(s):
    
    result = []
    s = s[2:-2].split('},{')
    s = sorted(s, key=lambda s : len(s))
    
    for i in range(len(s)):
            s[i] = s[i].split(',')
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in result:
                result.append(s[i][j])
    
    return list(map(int, result))