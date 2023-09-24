def solution(rsp):
    
    rsp_dict = dict(zip(['0','2','5'],['5','0','2']))
    
    return ''.join([rsp_dict[i] for i in rsp])
    