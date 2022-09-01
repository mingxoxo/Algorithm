# Julka
# 22.09.01
# https://www.acmicpc.net/problem/8437

import sys
input = sys.stdin.readline

apple = int(input())
diff = int(input())

print((apple - diff) // 2 + diff)
print((apple - diff) // 2)
