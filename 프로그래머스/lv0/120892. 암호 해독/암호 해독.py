def solution(cipher, code):
    
    
    return ''.join([cipher[i] for i in range(0, len(cipher)) if (i+1)%code==0])