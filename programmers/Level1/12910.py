#나누어 떨어지는 숫자 배열
#https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    if not answer:
        return [-1]
    return answer

#다른 사람의 풀이
#python은 or 앞이 참일경우 해당 값까지만 , 거짓일경우 뒤에 것까지 호출
#return sorted([n for n in arr if n%divisor == 0]) or [-1]
