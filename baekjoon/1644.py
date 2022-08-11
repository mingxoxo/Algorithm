# 소수의 연속합
# 22.08.12
# 투 포인터 / 에라토스테네스의 체
# https://www.acmicpc.net/problem/1644

import sys
input = sys.stdin.readline

def Sieve_of_Eratosthenes(N):
    is_prime = [1] * (N + 1)

    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i] == 1:
            for j in range(i+i, N+1, i):
                is_prime[j] = 0

    return [i for i in range(2, N + 1) if is_prime[i] == 1]

def two_pointer(prime_list, N, arr_len):
    start = 0
    end = 0
    cnt = 0
    arr_sum = 0

    while start <= end and end <= arr_len:
        if arr_sum < N:
            arr_sum += prime_list[end] if end < arr_len else 0
            end += 1
        else:
            if arr_sum == N:
                cnt += 1
            arr_sum -= prime_list[start]
            start += 1

    return cnt

def main():
    N = int(input())
    prime_list = Sieve_of_Eratosthenes(N)
    print(two_pointer(prime_list, N, len(prime_list)))

if __name__ == "__main__":
    main()
