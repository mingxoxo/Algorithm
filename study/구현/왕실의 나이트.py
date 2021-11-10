# 왕실의 나이트

y_s, x_s = list(input())
y_s = ord(y_s) - ord('a') + 1
x_s = int(x_s)

move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
numList = [i for i in range(1, 8+1)]
result = 0

for x, y in move:
    if x_s + x in numList and y_s + y in numList:
        result += 1

print(result)
