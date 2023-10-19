from itertools import permutations

def solution(k, dungeons):
    
    explore_list = []
    cases = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    
    for case in cases: # 0,1,2  0,2,1 ...
        temp_k = k
        explore_count = 0
        
        for i in range(len(case)):
            if temp_k >= dungeons[case[i]][0]:
                temp_k -= dungeons[case[i]][1]
                explore_count += 1
        explore_list.append(explore_count)
    
    return max(explore_list)
            
        
        