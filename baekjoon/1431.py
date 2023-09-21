# 시리얼 번호
# 정렬
# 23.09.21
# https://www.acmicpc.net/problem/1431

def sum_of_digits(serial_number):
    return sum([int(i) for i in serial_number if '0' <= i <= '9'])

N = int(input())
serial_number = [input() for _ in range(N)]
serial_number.sort(key=lambda x: (len(x), sum_of_digits(x), x))
print(*serial_number, sep="\n")
