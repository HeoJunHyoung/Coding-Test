def findYakNumber(x):
    yak_count = 0
    for i in range(1, int(x**(1/2))+1):
        if x % i == 0:
            yak_count += 1
            if ( (i**2) != x) : 
                yak_count += 1
    return yak_count


def solution(number, limit, power):
    
    return sum([findYakNumber(i) if findYakNumber(i)<=limit else power for i in range(1, number+1)])
    
