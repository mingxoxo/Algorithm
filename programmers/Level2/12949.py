# 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = []
    arr2_T = list(zip(*arr2)) #Transpose
    for a in arr1:
        answer.append([sum([i*j for i, j in zip(a, b)]) for b in arr2_T])
    return answer

#다른 사람의 풀이
#return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
