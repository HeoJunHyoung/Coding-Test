from collections import deque

def solution(queue1, queue2):
    
    total = sum(queue1) + sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    findValue = total // 2
    result = 0
    
    # 두 큐의 합이 홀수라서 같은 값으로 나뉘지 못하는 경우
    if total % 2 != 0:
        return -1
    
    # 찾아야 하는 값보다 큐 안의 한 원소가 더 커서 구하지 못하는 경우
    for q1 in queue1:
        if findValue < q1:
            return -1
    for q2 in queue2:
        if findValue < q2:
            return -1
    
    sum1, sum2 = sum(queue1), sum(queue2)
    final_recur = (len(queue1)+len(queue2)) * 4
    while sum1 != sum2:
        if sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        elif sum1 > sum2:
            sum2 += queue1[0]
            sum1 -= queue1[0]
            queue2.append(queue1.popleft())
        else:
            return result
        result += 1
        if result > final_recur:
            return -1
            
    
    return result
    