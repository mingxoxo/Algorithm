# 파일 정리
# 24.05.27
# https://www.acmicpc.net/problem/20291


from collections import defaultdict

N = int(input())
extension_dict = defaultdict(int)

for _ in range(N):
    extension = input().split('.')[-1]
    extension_dict[extension] += 1

for key in sorted(extension_dict.keys()):
    print(f'{key} {extension_dict[key]}')
