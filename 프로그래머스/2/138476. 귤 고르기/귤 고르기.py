def solution(k, tangerine):
    
    various = 0
    
    tangerine_set = list(set(tangerine))
    tangerine_dict = dict(zip(tangerine_set, [0]*len(tangerine)))
    for size in tangerine:
        tangerine_dict[size] += 1
    
    tangerine_dict = sorted(tangerine_dict.items(), reverse=True, key=lambda item:item[1])
    
    for value in tangerine_dict:
        various += 1
        if k <= value[1]:
            break
        k -= value[1]
        if k == 0:
            break
    
    return various