def solution(n, control):
    
    dictionary_control = dict(zip(['w','s','d','a'],[1,-1,10,-10]))
    for i in control:
        n += dictionary_control[i]
        
    return n