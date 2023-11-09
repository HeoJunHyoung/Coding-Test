from itertools import permutations

def checkSame(case, banned_id):
    
    for i in range(len(banned_id)):
        if len(banned_id[i]) != len(case[i]):
                return False
            
        for j in range(len(case[i])):
            if banned_id[i][j] == '*':
                continue
            else:
                if case[i][j] != banned_id[i][j]:
                    return False
    return True

def solution(user_id, banned_id):
    
    cases = list(permutations(user_id, len(banned_id)))
    result = []
    
    for case in cases:
        if not checkSame(case, banned_id):
            continue
        else:
            case = set(case)
            if case not in result:
                result.append(case)
    
    return len(result)