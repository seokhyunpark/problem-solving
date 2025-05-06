def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            s1 = s[left:right]
            if s1 == s1[::-1]:
                return 1
            s2 = s[left + 1: right + 1]
            if s2 == s2[::-1]:
                return 1
            else:
                return 2
    return 0


T = int(input())
for _ in range(T):
    print(is_palindrome(input()))
