'''
그냥 skill_tress에 있는 문자열들 하나씩 skill이랑 비교해가면서 진행하면 되지 않음?
어차피 최대 26*26*20*20 = 270,400 연산 이루어지니까
'''


def solution(skill, skill_trees):
    
    cnt = 0
    
    for skill_tree in skill_trees: # BACDE, CBADF, AECB, BDA
        i = 0
        flag = True
        for j in range(len(skill_tree)): # B A C D E 
            
            if skill_tree[j] in skill:
                if skill_tree[j] != skill[i]:
                    flag = False
                    break
                else:
                    i += 1
            else:
                continue
        if flag == True:
            cnt += 1
    
    return cnt
                    
            
    
            
    