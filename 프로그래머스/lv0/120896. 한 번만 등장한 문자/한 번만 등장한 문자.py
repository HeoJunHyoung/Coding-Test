def solution(s):
    answer = ''
    
    for i in range(0, len(s)):
        if s.count(s[i]) == 1:
            answer += s[i]
            
    return ''.join(sorted(answer))