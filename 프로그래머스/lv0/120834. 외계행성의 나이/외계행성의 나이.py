def solution(age):
    answer = ''
    alpa_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
                's','t','u','w','x','y','z']
    alpa_dict = dict(zip(list(range(0,len(alpa_list))), alpa_list))
    age = str(age)
    
    for i in range(0, len(age)):
        answer += alpa_dict[int(age[i])]
    
    return answer