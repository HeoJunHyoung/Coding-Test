



def solution(word):
    
    alpha = ['A','E','I','O','U', '']
    result = []
    
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for m in alpha:
                    for n in alpha:
                        tmp = i+j+k+m+n
                        # print(tmp)
                        if tmp not in result:
                            result.append(tmp)
    
    result = sorted(result)
    return result.index(word)
    
    