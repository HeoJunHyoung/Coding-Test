def solution(my_string, indices):
    
    my_string = list(my_string)
    for i in range(0, len(indices)):
        my_string[indices[i]] = ''
        
    return ''.join(my_string)
    
        
        
    