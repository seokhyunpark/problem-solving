s = input()

alphabets = [-1] * 26
for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    if alphabets[idx] == -1:
        alphabets[idx] = i

for alphabet in alphabets:
    print(alphabet, end=' ')
