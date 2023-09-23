def solution(s1, s2):
    
    result = 0
    for word in s1:
        result += s2.count(word)
        
    return result