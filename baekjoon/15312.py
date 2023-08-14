# 이름 궁합
# 23.08.14
# https://www.acmicpc.net/problem/15312

cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = input()
B = input()

love = []
for a, b in zip(A, B):
    love.append(cnt[ord(a) - ord('A')])
    love.append(cnt[ord(b) - ord('A')])

while len(love) != 2:
    love = [(love[i] + love[i + 1]) % 10 for i in range(len(love) - 1)]

print(*love, sep='')
