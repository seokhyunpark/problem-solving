string = input()

count_all_zero = 0
count_all_one = 0

if string[0] == '0':
    count_all_one += 1
elif string[0] == '1':
    count_all_zero += 1

for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        if string[i + 1] == '0':
            count_all_one += 1
        elif string[i + 1] == '1':
            count_all_zero += 1

print(min(count_all_zero, count_all_one))
