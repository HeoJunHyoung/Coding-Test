import heapq

def solution(operations):
    
    heap_list = []
    
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        
        if op == 'I':
            heapq.heappush(heap_list, num)
        elif op == 'D' and num == 1:
            if len(heap_list) != 0:
                max_value = max(heap_list)
                heap_list.remove(max_value)
        else:
            if len(heap_list) != 0:
                heapq.heappop(heap_list)
    
    if len(heap_list) == 0:
        return [0, 0]
    else:
        return [max(heap_list), heapq.heappop(heap_list)]