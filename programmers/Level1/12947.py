#하샤드 수
#https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    num = 0
    for i in list(map(int, str(x))):
        num += i
    answer = True if x%num == 0 else False
    return answer

#다른 사람의 풀이
#return n % sum([int(c) for c in str(n)]) == 0
