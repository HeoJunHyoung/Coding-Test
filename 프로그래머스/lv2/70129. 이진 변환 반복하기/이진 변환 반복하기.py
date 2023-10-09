def solution(s):
    answer = []
    deleted_zero = 0
    binary_trans = 0
    
    while s != '1':
        s_one = s.replace('0', '') # 111111
        deleted_zero += len(s)-len(s_one)
        
        s = bin(len(s_one))[2:] # 110
        binary_trans += 1
        
        #print(deleted_zero, binary_trans)
        #break
        
    return [binary_trans, deleted_zero]