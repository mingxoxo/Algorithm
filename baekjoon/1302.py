# 베스트셀러
# 23.05.16
# https://www.acmicpc.net/problem/1302


from collections import Counter

N = int(input())
book = sorted([input() for _ in range(N)])
print(Counter(book).most_common(1)[0][0])
