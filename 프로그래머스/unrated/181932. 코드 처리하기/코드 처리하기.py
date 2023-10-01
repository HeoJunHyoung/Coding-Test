def solution(code):
    ret = ''
    
    mode = 0
    idx = 0
    
    while idx <= len(code)-1:
        if mode == 0:
            if code[idx] != '1':
                if idx % 2 == 0:
                    ret += code[idx]
            else:
                mode = 1
            idx += 1
            
        else:
            if code[idx] != '1':
                if idx % 2 != 0:
                    ret += code[idx]
            else:
                mode = 0
            idx += 1
    
    return ret if ret else "EMPTY"