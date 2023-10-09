def solution(s):
    stack = []
    
    for word in s:
        stack.append(word)
        if len(stack)>=2:
            if stack[-1] == stack[-2]:
                stack.pop(-1)
                stack.pop(-1)
    return 0 if stack else 1