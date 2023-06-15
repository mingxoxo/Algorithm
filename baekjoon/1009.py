# 분산처리
# 23.06.15
# https://www.acmicpc.net/problem/1009
# 아이디어 공부: https://claude-u.tistory.com/248

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2 + 2
        print(a ** b % 10)
    else:
        b = b % 4 + 4
        print(a ** b % 10)

# 1의 자리 수 거듭제곱 반복 규칙
# 0: 10
# 1: 1
# 2: 2 4 8 6
# 3: 3 9 7 1
# 4: 4 6
# 5: 5
# 6: 6
# 7: 7 9 3 1
# 8: 8 4 2 6
# 9: 9 1
