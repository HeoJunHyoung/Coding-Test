m = int(input())
listA = list(map(int, input().split()))
k = int(input())

total_rock = sum(listA)
result = 0
probability = 1

for i in listA: # 5 6 7
    probability = 1
    for j in range(k): # 0 1
        probability = probability * (i-j) / (total_rock-j)
    result = result + probability 

print(result)