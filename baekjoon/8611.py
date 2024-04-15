# 팰린드롬 숫자
# 24.04.15
# 수학, 구현
# https://www.acmicpc.net/problem/8611


def convert_base(b, n):
    result = []
    
    while 0 < n:
        n, mod = divmod(n, b)
        result.append(str(mod))
    return result[::-1]


def is_palindrome(m):
    length = len(m)
    for i in range(length // 2):
        if m[i] != m[length - i - 1]:
            return False
    return True


n = int(input())
is_ans_exist = False

for i in range(2, 11):
    m = convert_base(i, n)
    if is_palindrome(m):
        print(i, ''.join(m))
        is_ans_exist = True
        
if not is_ans_exist:
    print("NIE")
