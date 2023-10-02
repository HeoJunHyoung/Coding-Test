def findGCD(boonja, boonmo):
    
    div_num = 2
    minNumber = min(boonja, boonmo)
    
    while div_num < minNumber:
        if boonja%div_num==0 and boonmo%div_num==0:
            boonja = boonja / div_num
            boonmo = boonmo / div_num
        else:
            div_num += 1
            
    return [boonja, boonmo]


def solution(numer1, denom1, numer2, denom2):
    
    boonja = numer1 * denom2 + numer2 * denom1
    boonmo = denom1 * denom2
    
    return findGCD(boonja, boonmo)


    