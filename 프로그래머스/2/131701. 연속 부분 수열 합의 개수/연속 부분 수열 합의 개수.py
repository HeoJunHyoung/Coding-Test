def solution(elements):
    
    end = len(elements)
    elements *= 2
    sum_list = []
    
    
    for bind in range(1, end):
        for i in range(0, end):
            sum_list.append(sum(elements[i:i+bind]))
    
    
    return len(set(sum_list))+1