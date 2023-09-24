n = int(input())
# print(n)

for i in range(1, n+1): # 0 1 2
    for j in range(0, i): # 0 1 2
        print('*', end='')
    print()    