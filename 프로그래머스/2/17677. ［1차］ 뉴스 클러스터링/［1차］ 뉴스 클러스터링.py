def solution(str1, str2):
    
    # 먼저 str1과 str2은 대,소문자 구분이 없으므로 upper 혹은 lower 수행
    str1, str2 = str1.upper(), str2.upper()
    
    # 각각을 2개씩 묶어야 함.
    arr1, arr2 = [], []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i]+str1[i+1])
            
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            arr2.append(str2[i]+str2[i+1])
    
    # 교집합의 개수 계산 : arr1과 arr2의 교집합을 구하고, 교집합의 원소들을 arr1과 arr2에 순회하면서 최소값을
    #                   중복 교집합으로 설정
    gyo_count = 0
    duples = set(arr1) & set(arr2)
    
    for duple in duples:
        gyo_count += min(arr1.count(duple), arr2.count(duple))
        
    
    # 합집합의 개수 계산
    hap_count = len(arr1)+len(arr2)-gyo_count
    
    # 최종결과
    
    if gyo_count==0 and hap_count!=0:
        return 0
    elif gyo_count==0 and hap_count==0:
        return 65536
    else:
        return int(gyo_count / hap_count * 65536) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    