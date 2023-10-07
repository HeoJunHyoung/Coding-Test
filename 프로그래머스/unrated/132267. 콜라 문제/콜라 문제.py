def solution(a, b, n):
    
    total = n
    new_cola = 0
    remain = 0
    
    while total >= a:
        
        new_cola = new_cola + total // a * b #실제로 내가 환급 받았던 콜라 수 (정답)
        print('new cola : {}'.format(new_cola))
        total = (total // a * b) + (total % a)
        print('total : {}'.format(total))
    
    return new_cola
    