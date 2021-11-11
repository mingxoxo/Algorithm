#https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def dfs(numbers, target, answer, index, result):
    if len(numbers) == index:
        if target == result:
            return answer+1
        else:
            return answer
    answer = dfs(numbers, target, answer, index+1, result-numbers[index])
    answer = dfs(numbers, target, answer, index+1, result+numbers[index])
    return answer
    

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0, 0)
    return answer
