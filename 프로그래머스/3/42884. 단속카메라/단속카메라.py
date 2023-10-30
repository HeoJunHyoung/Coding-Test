'''
카메라가 차량1과 차량2 사이에 있는 경우(카메라가 연결)
1. 1경로 안에 2경로가 있는 경우
2. 1경로 나가기전에 2경로가 있지만 넘어가는 경우

X. 1경로 끝보다 2경로 시작이 더 큰 경우는 카메라가 필요한 시점
'''
def solution(routes):
    cnt = 0
    criterion = -30001
    routes = sorted(routes, key = lambda x : (x[1], x[0]))
    
    for route in routes:
        if route[0] > criterion:
            cnt +=1
            criterion = route[1]
            
    return cnt
            