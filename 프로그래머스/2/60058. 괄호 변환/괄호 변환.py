def dfs(v):
    stack = []
    stack.append(v[0])
    
    for i in range(1, len(v)):
        stack.append(v[i])
        if stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()
            
    return False if stack else True
        
        

def solution(p):
    result = ''
    inc = 0
    #if dfs(list(p)):
        #return p
    while p:
        inc += 1
        u, v = '', ''
        left, right = 0, 0
        
        for i in range(len(p)):
            if p[i] == '(':
                u += '('
                left += 1
            else:
                right += 1
                u += ')'
            if left == right:
                v = p[len(u):]
                break
        
        # v가 빈 배열이거나 u가 올바른 괄호를 만족하지 못한다면,
        if dfs(u):
            result += u
            p = v[:]
            continue
            
        elif not dfs(u) or not v:
            temp = '(' + solution(v) + ')'
            u = u[1:-1]
            for i in range(len(u)):
                if u[i] == '(':
                    temp += ')'
                else:
                    temp += '('
            result += temp
        #print('u :',u, 'v :',v)
        
        if len(result) >= len(p):
            break
            
    return result
            
        