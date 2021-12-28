#https://www.acmicpc.net/problem/2023
#신기한 소수

#백트래킹(Backtracking)

import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

N = int(input()) #1 ~ 8

prime_number = [[] for _ in range(N)]
prime_number[0] = [2, 3, 5, 7]

for i in range(N-1):
    for num in prime_number[i]:
        for j in range(1, 10): #0은 고려할 필요가 없음 --> 2의 배수
            if is_prime(num * 10 + j):
                prime_number[i+1].append(num * 10 + j)

for i in prime_number[N-1]:
    print(i)
