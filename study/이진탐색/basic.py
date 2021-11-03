def binarySearch(array, target, start, end):
    if target < array[start]:
        return None
    mid = (end+start)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binarySearch(array, target, mid + 1, end)
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)



n, target = list(map(int, input().split()))
numList = list(map(int, input().split()))
a = binarySearch(numList, target, 0, n-1)
if a != None:
  print(a-1)
else:
  print(a)

