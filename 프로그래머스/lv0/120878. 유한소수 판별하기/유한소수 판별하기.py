def calcGiyak(a,b,criterion):
    i = 2
    while i <= criterion:
        if a%i==0 and b%i==0:
            a = a // i
            b = b // i
        i += 1
    return a,b



def solution(a, b):
    
    
    a,b = calcGiyak(a,b,min(a,b))
    div_num = 2
    num_list = []
    
    while div_num <= b:
        if b%div_num==0:
            b = b // div_num
            num_list.append(div_num)
        else:
            div_num += 1
    # print(num_list)
    num_set = list(set(num_list))
    # print(num_set)
    
    if 2 in num_set:
        del num_set[num_set.index(2)]
    if 5 in num_set:
        del num_set[num_set.index(5)]
    
    if not num_set:
        return 1
    else:
        return 2

    

    
            