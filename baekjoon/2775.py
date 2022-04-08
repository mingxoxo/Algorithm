#부녀회장이 될테야
#https://www.acmicpc.net/problem/2775

#파이썬3 통과 --> 이전 값을 변수에 저장해줌

#k층 n호
def resident(k, n, apart):
    # 종료 조건: 0층이거나 1호일 때
    if n == 1:
        return 1
    if k == 0:
        return n
    if k not in apart[n].keys():
        apart[n][k] = resident(k - 1, n, apart) + resident(k, n - 1, apart)

    return apart[n][k]

apart = [{} for i in range(15)]

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(resident(k, n, apart))
