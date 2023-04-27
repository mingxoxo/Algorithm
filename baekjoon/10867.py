# 중복 빼고 정렬하기
# 23.04.27
# https://www.acmicpc.net/problem/10867

N = int(input())
num = sorted(list(set(map(int, input().split()))))
print(*num)
