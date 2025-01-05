# 엑셀
# 25.01.05
# https://www.acmicpc.net/problem/2757


import sys
input=sys.stdin.readline

while True:
    info = input().rstrip()
    if info == 'R0C0':
        break
    r, c = info.split('C')
    c = int(c)
    
    rev_base = ''
    while c > 0:
        c -= 1
        c, mod = divmod(c, 26)
        rev_base += chr(ord('A') + mod)
    
    print(rev_base[::-1] + r[1:])
