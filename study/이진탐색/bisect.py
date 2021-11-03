from bisect import bisect_left, bisect_right
#수열은 항상 오름차순

N, x = list(map(int, input().split()))
element = list(map(int, input().split()))

left_index = bisect_left(element, x)
right_index = bisect_right(element, x)
count = right_index-left_index
if count == 0:
    print(-1)
else:
    print(count)
