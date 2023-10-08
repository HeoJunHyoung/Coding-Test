def solution(s):
    
    stack = []
    
    for i in s:
        stack.append(i)
        if len(stack)>=2:
            if stack[-1] == ')' and stack[-2] == '(':
                del stack[-1]
                del stack[-1]
    if not stack:
        return True
    else:
        return False