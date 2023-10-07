def solution(X, Y):
    answer = ''
    X_temp=list(set(X))
    
    for i in range(0, len(X_temp)):
        if X_temp[i] in Y:
            count = min(X.count(X_temp[i]), Y.count(X_temp[i]))
            answer += X_temp[i]*count
    
    if not answer:
        return '-1'
    elif answer.count('0') == len(answer):
        return '0'
    else:    
        return ''.join(sorted(answer, reverse=True))