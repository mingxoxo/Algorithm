#셀프 넘버
#https://www.acmicpc.net/problem/4673

def d(n):
    sum = n
    while n > 0:
        sum += n%10
        n = n//10
    return sum

number_list = [i for i in range(1, 10001)]

not_self_number = map(d, number_list)

self_number = sorted(list(set(number_list) - set(not_self_number)))
for i in self_number:
    print(i)
