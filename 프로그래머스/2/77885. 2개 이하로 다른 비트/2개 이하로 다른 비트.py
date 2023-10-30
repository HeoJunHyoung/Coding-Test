
'''
제한사항 numbers의 길이가 10^5라서 이중 반복문을 이용하면 안됨

1. 값이 짝수 일때는 마지막 자릿수의 값이 0이고 자릿수 변환이 없기 때문에 마지막만 0에서 1로 변환하면 정답처리 됨
2. 값이 홀수 일때는 마지막 '0'을 '1'로 바꾸고, 그 다음 인덱스의 값을 '0'으로 변경
'''

def solution(numbers):
    
    result = []
    
    for number in numbers:
        converted = bin(number)[2:]
        #print(converted)
        
        # 짝수
        if int(converted, 2) % 2 == 0:
            converted = converted[:-1] + '1'
        # 홀수
        else:
            converted = '0' + converted[:]
            last_zero_idx = converted.rfind('0')
            converted = list(converted)
            converted[last_zero_idx], converted[last_zero_idx+1] = '1', '0'
            converted = ''.join(converted)
            
        result.append(int(converted, 2))
    
    return result