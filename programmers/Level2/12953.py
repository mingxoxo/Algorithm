#N개의 최소공배수
#https://programmers.co.kr/learn/courses/30/lessons/12953

def lcm(n, m): #최소공배수
    max_num = n if n > m else m
    while max_num%n != 0 or max_num%m != 0:
        max_num += 1
    return max_num

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer

#최대공약수를 이용해서 최소공배수를 구하는 공식
#lcm(a, b) = (a*b)/gcd(a, b)

#다른 사람의 풀이
# def gcd(a, b): --> 유클리드 호제법
#     if b == 0:
#         return a
#     return gcd(b, a%b)


# def nlcm(num):
#     num.sort()
#     max_num = num[-1]
#     # print (num, max_num)
#     temp = 1
#     for i in range(len(num)):
#         # lcm = (a*b) / gcd
#         # gcd = (a*b) / lcm
#         temp = (num[i] * temp) / (gcd(num[i], temp))
#         # print (temp)
#     return temp
