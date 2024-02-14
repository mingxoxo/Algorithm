# 1의 개수 세기
# 24.02.14
# 누적합
# https://www.acmicpc.net/problem/9527

prefix_sum = [0, 1, 4]

def init_prefix_sum_arr(B):
    global prefix_sum
    
    num = 8 # 2**3
    while num <= B:
        prefix_sum.append(num // 2 + 2 * prefix_sum[-1])
        num *= 2

def get_prefix_sum(n):
    global prefix_sum
    
    result = 0
    while n:
        bin_len = len(bin(n)[2:]) - 1
        result += prefix_sum[bin_len] + 1
        result += n - 2 ** bin_len
        n -= (2 ** bin_len)
    
    return result



A, B = map(int, input().split())
init_prefix_sum_arr(B)
print(get_prefix_sum(B) - get_prefix_sum(A - 1))
