#한수
#https://www.acmicpc.net/problem/1065

def fun(n):
    num = list(str(n))
    sub_list = [int(num[i+1]) - int(num[i]) for i in range(len(num)-1)]
    if not sub_list or len(set(sub_list)) == 1:
        return 1
    return 0

N = int(input())
print(sum(map(fun, [i for i in range(1, N+1)])))
