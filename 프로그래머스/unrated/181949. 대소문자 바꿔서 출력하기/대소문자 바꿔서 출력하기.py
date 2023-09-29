str = input()
answer = ''

for i in range(0, len(str)):
    if str[i] > 'Z':
        answer += str[i].upper()
    else:
        answer += str[i].lower()
    
print(answer)