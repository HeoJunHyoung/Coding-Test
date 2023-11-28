def solution(progresses, speeds):
        
    finish_day = [(100-progresses[i])//speeds[i] if (100-progresses[i])%speeds[i]==0 else (100-progresses[i])//speeds[i]+1 for i in range(len(progresses))]
    result = []
    
    idx = 0
    while idx < len(progresses):
        criterion_value = finish_day[idx] # 9
        cnt = 0
        
        while criterion_value >= finish_day[idx]:
            idx += 1
            cnt += 1
            if idx >= len(progresses):
                break
        result.append(cnt)
    
    return result