# 베르트랑 공준
# 24.07.31
# 에라토스테네스의 체
# https://www.acmicpc.net/problem/4948

import sys
input=sys.stdin.readline

def prime_numbers(n=123456 * 2):
    check_prime_numbers = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if check_prime_numbers[i] == False:
            continue
        
        for j in range(i+i, n + 1, i):
            check_prime_numbers[j] = False

    return check_prime_numbers
    

check_prime_numbers = prime_numbers()
while True:
    n = int(input())
    if n == 0:
        break
    print(sum(check_prime_numbers[n+1:2*n+1]))
