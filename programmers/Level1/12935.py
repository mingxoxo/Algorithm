#제일 작은 수 제거하기
#https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []
    arr.remove(min(arr))
    answer = [-1] if not arr else arr
    return answer
