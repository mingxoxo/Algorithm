# 한국이 그리울 땐 서버에 접속하지
# 문자열
# 23.12.02
# https://www.acmicpc.net/problem/9996

N = int(input())
pattern = input()
start_str, end_str = pattern.split('*')
for _ in range(N):
    string = input()
    print("DA") if len(pattern) - 1 <= len(string) and string.startswith(start_str) and string.endswith(end_str) else print("NE")
