def solution(numlist, n):
    
    gap_list = [abs(i-n) for i in numlist]
    result = []
    
    print(gap_list)
    
    sorted_gap_list = sorted(gap_list)
    print(sorted_gap_list)
    
    for i in range(0, len(sorted_gap_list)):
        if sorted_gap_list.count(sorted_gap_list[i]) == 1:
            result.append(numlist[gap_list.index(sorted_gap_list[i])])
        else:
            max_idx = -1
            max_value = -1
            for j in range(0, len(gap_list)):
                if sorted_gap_list[i] == gap_list[j]: # 1
                    if max_value < numlist[j]:
                        max_value = numlist[j]
                        max_idx=j
                    
            gap_list[max_idx] = -1
            result.append(numlist[max_idx])
    
    return result