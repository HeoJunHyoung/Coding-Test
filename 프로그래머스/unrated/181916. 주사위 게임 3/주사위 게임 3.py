def solution(a, b, c, d):
    
    total = 0
    result = 1
    dice_freq = [0]*6
    # print(dice_freq)
    
    dices = [a,b,c,d]
    for i in dices:
        dice_freq[i-1] += 1
    print(dice_freq)
    
    large_freq = max(dice_freq)
    
    if large_freq == 1:
        return min(dices)
    elif large_freq == 4:
        return 1111*(dice_freq.index(4)+1)
    elif large_freq == 3:
        return (10 * (dice_freq.index(3)+1) + dice_freq.index(1)+1)**2
    else:
        if dice_freq.count(2) == 2:
            pq = [i+1 for i in range(len(dice_freq)) if dice_freq[i]==2]
            return (pq[0]+pq[1])*abs((pq[0]-pq[1]))
        else:
            for i in range(0, len(dice_freq)):
                if dice_freq[i] == 1:
                    result *= (i+1)
        return result
    