# Adding Commas
# 24.04.16
# https://www.acmicpc.net/problem/5949
# python format 함수 쓰면 한 줄로도 구현 가능

# 이전 풀이
# def add_comma(string):
#     str_len = len(string)
#
#     result = []
#     reversed_string = list(reversed(string))
#     while str_len > 0:
#         mod = str_len % 3 if str_len % 3 else 3
#         for _ in range(mod):
#             result.append(reversed_string.pop())
#         result.append(',')
#         str_len -= mod
#     result.pop()
#
#     return ''.join(result)

# 고친 풀이
def new_add_comma(string):
    result = []
    str_len = len(string)
    for i in range(str_len):
        result.append(string[i])
        if (str_len - (i + 1)) % 3 == 0 and i + 1 != str_len:
            result.append(',')
    return ''.join(result)

N = input()
print(new_add_comma(N))
