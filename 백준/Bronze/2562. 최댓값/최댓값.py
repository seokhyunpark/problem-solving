arr = [int(input()) for _ in range(9)]

max_num = max(arr)
max_idx = arr.index(max_num) + 1

print(max_num)
print(max_idx)
