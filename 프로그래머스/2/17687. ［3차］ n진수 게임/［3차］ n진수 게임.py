'''
1. 먼저 주어진 값의 진수 별 값을 구해서 리스트에다가 때려박음
2. 미리 구할 숫자의 갯수(t)와 게임에 참가하는 인원(m)의 곱이 리스트 순회의 최대 순회값이기 때문에 t*m만큼 리스트를 순회
3. 리스트에서 꺼내서 answer라는 리스트에 넣고 리턴해주면 끝일거 같은디?
'''

def convert(listX, n, k):
    if n == 0:
        listX.append('0')
    else:
        temp = ''
        while n > 0:
            n, mod = divmod(n, k)
            # 값이 10 이상, 15 이하는 A~F로 출력
            if mod >= 10:  # Corrected condition
                temp += chr(ord('A') + mod - 10)

            else: 
                temp += str(mod)
        
        listX.append(temp[::-1])

    return listX


def solution(n, t, m, p):
    
    listX = []
    answer = []
    for i in range(t*m):
        listX = convert(listX, i, n)
    listX = ''.join(listX)

    for i in range(p-1, t*m, m):
        answer.append(listX[i])
    
    return ''.join(answer)

