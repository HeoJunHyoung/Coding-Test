def solution(balls, share):
    
    n_factorial = 1
    m_factorial = 1
    n_m_factorial = 1
    
    for i in range(balls, 0, -1):
        n_factorial *= i
    
    for i in range(share, 0, -1):
        m_factorial *= i
    
    for i in range(balls-share, 0, -1):
        n_m_factorial *= i 
    
    return n_factorial/(m_factorial*n_m_factorial)