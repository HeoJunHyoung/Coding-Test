def solution(str_list, ex):
    
    newList = []
    
    for i in range(0, len(str_list)):
        if ex not in str_list[i]:
            newList.append(str_list[i])
            
    return ''.join(newList)