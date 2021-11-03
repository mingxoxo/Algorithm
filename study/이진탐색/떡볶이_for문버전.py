N, M = list(map(int, input().split()))
ricecake = list(map(int, input().split()))

ricecake.sort() #정렬
cutHeight = max(ricecake)

for i in range(max(ricecake) - M, max(ricecake)):
    cut = list(map(lambda x: x - i if x > i else 0, ricecake))
    if sum(cut) < M:
        cutHeight = i - 1
        break
print(cutHeight)


