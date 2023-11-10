'''
윈도우 슬라이싱으로 for문 돌려보려고 했는데 시간 초과날게 뻔함..
못 찾아서 답지 봤음
'''
from collections import Counter

def solution(topping):
    
    young = Counter(topping)
    old = dict()
    cnt = 0
    
    for i in topping:
        young[i] -= 1
        if young[i] == 0:
            del young[i]
        if i in old:
            old[i] += 1
        else:
            old[i] = 1
        if len(old) == len(young):
            cnt += 1
        
        
    return cnt
    
    