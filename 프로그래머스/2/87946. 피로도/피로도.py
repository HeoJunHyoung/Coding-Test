from itertools import permutations

def solution(k, dungeons):
    cases = list(permutations(dungeons, len(dungeons)))
    result = 0
    #print(cases)
    
    for case in cases:
        current_fatigue = k
        possible = 0
        for i in range(len(case)):
            if current_fatigue >= case[i][0]:
                current_fatigue -= case[i][1]
                possible += 1
            else:
                break
        result = max(possible, result)
    return result