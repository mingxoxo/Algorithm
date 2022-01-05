#행렬의 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        answer.append(list(x[i]+y[i] for i in range(len(x))))
    return answer

#다른 사람의 풀이
#answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
