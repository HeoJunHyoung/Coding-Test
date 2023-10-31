'''
D[i]는 아파트에서 필요한 최소 기지국 수
D[i] = 
최소 기지국 설치 수는

if (회색 범위:R) % (W * 2) != 0:
    cnt += (R//(W*2)) + 1
else:
    cnt += R // (W*2)
'''

def solution(n, stations, w):
    
    cnt = 0
    already_located_start = 0
    already_located_end = 0
    
    for station in stations:
        
        already_located_start = station - w # 
        increase = already_located_start - 1 - already_located_end # 
        already_located_end = station + w # 
        print(increase)
        if increase % (w*2+1) != 0:
            cnt += increase//(w*2 + 1) + 1 #
        else:
            cnt += increase // (w*2+1)
        print(cnt)
        print()
        
    if already_located_end < n:
        increase = n - already_located_end
        #print(increase)
        if increase % (w*2+1) != 0:
            cnt += increase//(w*2+1) + 1
        else:
            cnt += increase // (w*2+1)
    
    
    return cnt
    
    
    
    
    