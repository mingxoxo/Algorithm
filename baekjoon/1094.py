# 막대기
# 23.05.29
# 수학, 비트마스킹
# https://www.acmicpc.net/problem/1094

# 풀이 1
X = int(input())
bar = 64
cnt = 0
while X:
    while X < bar:
        bar //= 2
    X -= bar
    cnt += 1

print(cnt)

# 풀이 2
# print(bin(int(input())).count('1'))

# 풀이 3
# print(int(input()).bit_count())
# https://docs.python.org/ko/3.10/library/stdtypes.html
