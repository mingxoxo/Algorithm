#소수 구하기
#https://www.acmicpc.net/problem/1929

#에라토스테네스의 체

def prime_number(M, N):
    num_list = [i for i in range(N+1)]
    check = [True] * len(num_list)
    for i in range(2, len(num_list)):
        if check[i] == False:
            continue
        for j in range(i+i, len(num_list), i):
            check[j] = False
    M = 2 if M == 1 else M
    return [i for i in range(M, len(num_list)) if check[i] == True]



M, N = map(int, input().split())
for i in prime_number(M, N):
    print(i)
