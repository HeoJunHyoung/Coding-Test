def solution(id_pw, db):
    answer = ''
    
    for i in range(0, len(db)):
        for j in range(0, len(db[i])):
            if id_pw[0] != db[i][0] and id_pw[1] != db[i][1]:
                answer = 'fail'
            elif id_pw[0] == db[i][0] and id_pw[1] != db[i][1]:
                answer = 'wrong pw'
            elif id_pw[0] == db[i][0] and id_pw[1] == db[i][1]:
                answer = 'login'
            
            
    
    
    return answer