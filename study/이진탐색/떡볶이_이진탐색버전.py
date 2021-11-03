def binarySearch(array, target, start, end, result):
    mid = (end + start) // 2
    cut = list(map(lambda x: x - mid if x > mid else 0, array))
    if sum(cut) >= target:
        result = mid
    if start >= end:
        return result
    if sum(cut) > target:
        return binarySearch(array, target, mid + 1, end, result)
    elif sum(cut) < target:
        return binarySearch(array, target, start, mid - 1, result)

N, M = list(map(int, input().split()))
ricecake = list(map(int, input().split()))

ricecake.sort() #정렬
a = binarySearch(ricecake, M, max(ricecake)-M, max(ricecake), max(ricecake)-M)
print(a)



