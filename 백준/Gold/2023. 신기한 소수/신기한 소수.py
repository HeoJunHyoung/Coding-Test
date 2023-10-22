def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

n = int(input())

stack = [[str(i), int(i)] for i in range(0, 10) if isPrime(i)]
result = []
#print(stack)

while stack:
    prime_number_str, prime_number = stack.pop()

    if len(prime_number_str) == n:
        result.append(prime_number)
    else:
        for i in range(10):
            temp_str = prime_number_str + str(i)
            temp = 10*prime_number + i

            if isPrime(temp):
                stack.append([temp_str, temp])

result = sorted(result)

for i in range(len(result)):
    print(result[i])
