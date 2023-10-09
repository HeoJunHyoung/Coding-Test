def solution(dots):
    
    couple = ['0123', '0213', '1203']
    #print(couple)
    
    for i in range(len(couple)): # 0 1 2
        line1 = (dots[int(couple[i][0])][0]-dots[int(couple[i][1])][0]) / (dots[int(couple[i][0])][1]-dots[int(couple[i][1])][1])
        line2 = (dots[int(couple[i][2])][0]-dots[int(couple[i][3])][0]) / (dots[int(couple[i][2])][1]-dots[int(couple[i][3])][1])
        print(line1, line2)
        
        if line1 == line2:
            return 1
    return 0