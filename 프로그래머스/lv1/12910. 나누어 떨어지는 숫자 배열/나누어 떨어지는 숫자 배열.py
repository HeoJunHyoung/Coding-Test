def solution(arr, divisor):
    answer = [i for i in arr if i%divisor==0]
    answer = sorted(answer)
    return answer if answer else [-1]