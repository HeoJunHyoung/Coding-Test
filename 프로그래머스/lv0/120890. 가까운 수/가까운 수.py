def solution(array, n):
    minimum = 101
    gap_list = [array[i]-n if array[i]>n else n-array[i] for i in range(0, len(array))]
    
    min_value = min(gap_list)
    
    if gap_list.count(min_value) >= 2:
        for i in range(0, len(gap_list)):
            if gap_list[i] == min_value:
                if minimum > array[i]:
                    minimum = array[i]
        return minimum
    
    
    else:
        return array[gap_list.index(min_value)]