def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] < array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            array[pivot], array[right] = array[right], array[pivot]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))

quick_sort(num_list, 0, len(num_list)-1)
for i in num_list:
    print(i)



