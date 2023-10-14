def solution(n, lost, reserve):
    
    students = [2 for i in range(n)]
    #print(students)
    
    lost_list, reserve_list = list(set(lost)-set(reserve)), list(set(reserve)-set(lost))
    lost, reserve = sorted(lost_list), sorted(reserve_list)
    
    # own:2 / reserve:1 / lost:0
    for i in range(len(lost)):
        students[lost[i]-1] = 0
    for i in range(len(reserve)):
        students[reserve[i]-1] = 1
        
    for i in range(n):
        if students[i] == 2 or students[i]==1:
            continue
        else:
            if students[max(i-1, 0)] == 1:
                students[max(i-1, 0)] = 2
                students[i] = 2
            elif students[min(i+1, len(students)-1)] == 1:
                students[min(i+1, len(students)-1)] = 2
                students[i] = 2
            
    
    return students.count(1) + students.count(2)              
                
                
                
                
                