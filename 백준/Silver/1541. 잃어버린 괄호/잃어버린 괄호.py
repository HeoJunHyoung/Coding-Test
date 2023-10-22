problem = input()

splited = problem.split('-')
#print(splited)
answer = 0

for index, value in enumerate(splited):
    again = list(map(int, value.split('+')))

    if index == 0:
        answer += sum(again)
    else:
        answer -= sum(again)

print(answer)