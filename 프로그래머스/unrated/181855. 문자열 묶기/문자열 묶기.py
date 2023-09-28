def solution(strArr):
    
    dict_str = dict(zip(range(0, 31), [0]*31))
    
    for i in range(0, len(strArr)):
        dict_str[len(strArr[i])] += 1
    
    return max([dict_str[value] for value, key in dict_str.items()])
    # max(dict_str)