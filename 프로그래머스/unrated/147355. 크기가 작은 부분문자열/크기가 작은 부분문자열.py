def solution(t, p):
    answer = 0
    
    for i in range(0, len(t)-len(p)+1):
        pick_num = int(t[i:i+len(p)])
        if pick_num <= int(p):
            answer += 1
    
    return answer