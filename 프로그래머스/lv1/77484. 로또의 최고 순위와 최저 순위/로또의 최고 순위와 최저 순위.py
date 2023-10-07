def solution(lottos, win_nums):
    
    same = 0
    unknown = lottos.count(0)
    order = dict(zip(list(range(6,-1,-1)),list(range(1,7))))
    order[0]= 6
    
    for i in lottos:
        if i in win_nums:
            same += 1
            
    max_win = same + unknown
    min_win = same
    
    #print(max_win, min_win)
    #print(order[max_win])
    
    return [order[max_win], order[min_win]]
    
    