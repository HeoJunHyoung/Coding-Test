def solution(rsp):
    
    rsp_dict = dict(zip(['0','2','5'],['5','0','2']))
    newList = []
    result = None
    
    for i in range(0, len(rsp)):
        newList.append(rsp_dict[rsp[i]])
        
    return ''.join(newList)
    
    