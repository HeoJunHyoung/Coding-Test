def solution(N, stages):
    
    
    result = []
    fail_rate_list = []
    n = len(stages)
    
    for i in range(N):
        stage_freq = stages.count(i+1)
        fail_rate_list.append(stage_freq/n)
        
        n = n - stage_freq
        if n==0:
            n = stage_freq = stages.count(i+1)
        print(stage_freq, n)
    
    sorted_fail_rate_list = sorted(fail_rate_list, reverse=True)
    
    for i in range(len(sorted_fail_rate_list)):
        result.append(fail_rate_list.index(sorted_fail_rate_list[i])+1)
        fail_rate_list[fail_rate_list.index(sorted_fail_rate_list[i])] = -1
    
    return result
    
    
    