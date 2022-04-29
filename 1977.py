
M = int(input())
N = int(input())

start_value = int(M ** 0.5) if int(M ** 0.5) ** 2 == M else int(M ** 0.5) + 1
end_value = int(N ** 0.5)
min_value = start_value ** 2
sum_value = 0
if start_value >= end_value:
    print(-1)
else:
    for value in range(start_value, end_value + 1):
        sum_value += value ** 2

    print(f'{sum_value}\n{min_value}')