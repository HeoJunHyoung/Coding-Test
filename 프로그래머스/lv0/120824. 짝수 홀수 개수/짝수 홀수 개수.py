def solution(num_list):
    
    evenList = [i for i in num_list if i % 2 == 0]
    
    return [len(evenList), len(num_list) - len(evenList)]