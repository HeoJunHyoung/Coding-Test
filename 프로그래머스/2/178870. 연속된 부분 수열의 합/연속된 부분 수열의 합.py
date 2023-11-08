'''
문제 보자마자 생각난건 start와 end가 0부터 시작하는 투포인터 알고리즘
'''

def solution(sequence, k):
    result = []
    sequence.append(0)
    start, end = 0, 1
    total = sequence[start] + sequence[end]
    if sequence[0] == k:
        result.append([0, 0])
    while end != len(sequence)-1 and start != len(sequence)-1 :
        
        if total < k:
            end += 1
            total += sequence[end]
        
        elif total > k:
            total -= sequence[start]
            start += 1
            
        else:
            result.append((start, end))
            end += 1
            total += sequence[end]
        
    order = [result[i][1]-result[i][0] for i in range(len(result))]
    return result[order.index(min(order))]
            
        
        
        
        
        
        
        
            