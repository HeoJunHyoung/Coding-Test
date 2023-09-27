def solution(n):
    
    pizza_count = 1
    
    while n * pizza_count % 6 != 0: # 10 * 1 % 6, 10 * 2 % 6, 10 * 3 
        pizza_count += 1
    
    return pizza_count * n / 6 