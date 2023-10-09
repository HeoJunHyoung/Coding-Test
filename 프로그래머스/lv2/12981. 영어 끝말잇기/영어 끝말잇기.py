def solution(n, words):
    
    stack = []
    for i in range(len(words)-1):
        stack.append(words[i])
        if words[i][-1] != words[i+1][0] or words[i+1] in stack:
            #print(words[i+1])
            print(i+2)
            if (i+2)/n > (i+2)//n:
                return [(i+1)%n+1, (i+2)//n+1]
            else:  
                return [(i+1)%n+1, (i+2)//n]
    return [0, 0]