def solution(my_string):
    
    fullAlpaString = 'abcdefghijklmnopqrstuvwxyz'.upper() + 'abcdefghijklmnopqrstuvwxyz'
    
    orderList = [0]*52
    alpa_dict = dict(zip(list(fullAlpaString),orderList))
    
    for i in range(0, len(my_string)):
        alpa_dict[my_string[i]] += 1
    
    
    return [alpa_dict[key] for key, value  in alpa_dict.items()] 
