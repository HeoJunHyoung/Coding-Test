def solution(polynomial):
    
    polynomial = polynomial.split(' ')
    # print(polynomial)
    
    xList = []
    const = []
    
    for i in range(0, len(polynomial), 2):
        if 'x' in polynomial[i]:
            if polynomial[i] == 'x':
                polynomial[i] = '1x'
            xList.append(polynomial[i])
        else:
            const.append(polynomial[i])
            
    
    x = 0
    sangsoo = 0
    
    for i in range(0, len(xList)):
        x += int(xList[i][:-1])
    
    for i in range(0, len(const)):
        sangsoo += int(const[i])
    
    print(x)
    print(sangsoo)
    
    if sangsoo != 0:
        if x == 0:
            return str(sangsoo)
        elif x == 1:
            return 'x + '+str(sangsoo)
        else:
            return str(x)+'x + '+str(sangsoo)
    
    else:
        if x == 0:
            return '0'
        elif x == 1:
            return 'x'
        else:
            return str(x)+'x'
    
    
    
    
    
    
    
    
    
    