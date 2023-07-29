# 링
# 23.07.29
# 유클리드 호제법
# https://www.acmicpc.net/problem/3036


def euclidean(a, b):
    while b > 0:
        a, b = b, a % b

    return a


N = int(input())
ring, *others = list(map(int, input().split()))

for i in others:
    gcd = euclidean(ring, i)
    print('{0}/{1}'.format(ring//gcd, i//gcd))
