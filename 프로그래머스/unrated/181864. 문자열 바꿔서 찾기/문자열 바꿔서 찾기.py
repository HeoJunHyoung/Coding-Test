def solution(myString, pat):
    
    alpa_dict = dict(zip(['A','B'],['B','A']))
    
    newString = ''.join([alpa_dict[i] for i in myString])
    
    return 1 if pat in newString else 0