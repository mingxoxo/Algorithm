# 스위치 켜고 끄기
# 구현
# 23.09.11
# https://www.acmicpc.net/problem/1244

N = int(input())
switch = list(map(int, input().split()))
for _ in range(int(input())):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(number, N + 1, number):
            switch[i - 1] ^= 1
    elif gender == 2:
        switch[number - 1] ^= 1
        left, right = number - 2, number
        while True:
            if left < 0 or N <= right:
                break
            if switch[left] != switch[right]:
                break
            switch[left] = switch[right] = switch[right] ^ 1
            left -= 1
            right += 1

for i in range(N // 20 + 1):
    print(*switch[i * 20:(i + 1) * 20])
