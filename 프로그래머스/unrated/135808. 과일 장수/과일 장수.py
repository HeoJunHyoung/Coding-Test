def solution(k, m, score):
    
    result = 0
    score = sorted(score, reverse=True)
    box_number = len(score) // m    # 4
    box_list = []
    
    for i in range(0, len(score), m):
        box_list.append(score[i:i+m])
    
    if len(box_list) != box_number:
        del box_list[-1]
    
    return sum([min(box_list[i])*m for i in range(len(box_list))])