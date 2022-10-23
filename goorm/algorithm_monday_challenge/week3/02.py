# 문제 2. 폴더 폰 자판
# 구현 / 문자열

key = [[], [5, "1.,?!"], [4, "2ABC"], [4, "3DEF"],
       [4, "4GHI"], [4, "5JKL"], [4, "6MNO"],
       [5, "7PQRS"], [4, "8TUV"], [5, "9WXYZ"]]

n = int(input())
s = input()

i = 0

while i < len(s):
    num = int(s[i])
    j = i + 1
    while j < len(s) and s[i] == s[j]:
        j += 1

    print(key[num][1][(j - i - 1) % key[num][0]], end="")
    i = j
