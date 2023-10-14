def solution(s, skip, index):
    answer = ''
    
    for word in s: # 'y'
        real_index = index # 1
        
        while real_index != 0:
            if ord(word)+1 > ord('z'):
                word = chr(ord('a') - 1 )
            
            
            if chr(ord(word)+1) not in skip: # 
                word = chr(ord(word)+1)
                real_index -= 1
            else:
                word = chr(ord(word)+1)
            
        answer += word
        
    return answer