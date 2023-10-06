def solution(s, n):
    
    answer = ''
    
    for alpha in s:
        if not alpha.isalpha():
            answer += alpha
        #대문자
        if ord(alpha)>=65 and ord(alpha)<=90:
            if ord(alpha)+n>90:
                answer += chr((ord(alpha)+n-1)-25)
            else:
                answer += chr(ord(alpha)+n)
        
        #소문자
        if ord(alpha)>=97 and ord(alpha)<=122:
            if ord(alpha)+n>122:
                answer += chr((ord(alpha)+n-1)-25)
            else:
                answer += chr(ord(alpha)+n)
    
    
    return answer