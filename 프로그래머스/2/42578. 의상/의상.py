def solution(clothes):
    # {종류 : 의상 이름} 딕셔너리 생성
    # len(dictionary)는 한 종류의 의상만 선택한 모든 경우의 수를 의미
    
    # len(dictionary[0~i])는 각 종류 별 존재하는 의상들의 개수를 의미
    # 각 종류 별 존재하는 의상들의 개수를 리스트로 변환
    # 변환된 리스트들의 값들을 모두 곱하면 
    
    cloth_dict = dict()
    answer = 1
    
    for i in range(len(clothes)):
        if clothes[i][1] in cloth_dict:
            cloth_dict[clothes[i][1]] += 1
        else:
            cloth_dict[clothes[i][1]] = 1
            
    for value in cloth_dict.values():
        answer = answer * (value+1)
    
    return answer-1