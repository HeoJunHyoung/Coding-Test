ingredient_number = int(input())

total_armor = int(input())

ingredients = sorted(list(map(int, input().split())))

left, right = 0, len(ingredients)-1
count = 0

while left < right:

    weight = ingredients[left] + ingredients[right]

    if weight < total_armor:
        left += 1
    elif weight > total_armor:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1

print(count)