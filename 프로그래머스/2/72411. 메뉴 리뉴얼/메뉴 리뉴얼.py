from itertools import combinations

def solution(orders, course):
    
    
    result = []
        
    for group in course: # 2 3 4
        course_freq = dict()
        temp = []
        for order in orders:
            cases = list(combinations(order, group))
            for c in cases:
                c = ''.join(sorted(c))
                #print(c)
                if c not in course_freq:
                    course_freq[c] = 1
                else:
                    course_freq[c] += 1
        if course_freq:
            before = sorted(course_freq.items(), reverse=True, key = lambda x : x[1])
            if before[0][1] >= 2:
                max_freq = before[0][1]
                temp = [before[i][0] for i in range(len(before)) if before[i][1] >= max_freq]
        result.extend(temp)
    
    return sorted(result)
            
                
            
            
            
            
            