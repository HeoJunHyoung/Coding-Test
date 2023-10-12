def solution(elements):
    
    origin = elements[:]
    end = len(elements)
    elements *= 2
    sum_list = []
    
    #print(end)
    #print(elements)
    
    
    for bind in range(1, end): # 1 2 3 4 5
        for i in range(0, end): # 0 1 2 3 4
            sum_list.append(sum(elements[i:i+bind]))
    
    sum_list.append(sum(origin))
    
    return len(set(sum_list))