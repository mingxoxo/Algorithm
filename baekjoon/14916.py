# 거스름돈
# 그리디
# 23.08.28
# https://www.acmicpc.net/problem/14916


n = int(input())
five = n // 5

while 0 <= five:
    if (n - five * 5) % 2 == 0:
        print(five + (n - five * 5) // 2)
        break
    five -= 1

if five < 0:
    print(-1)
