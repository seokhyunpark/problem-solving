import math

M, N = map(int, input().split())

prime_numbers = []
for i in range(max(M, 2), N + 1):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)

for number in prime_numbers:
    print(number)
