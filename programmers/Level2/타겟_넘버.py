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

## 다른 사람의 풀이 중 깔끔하게 재귀로 푼 코드  
# def solution(numbers, target):
#     if not numbers and target == 0: #만약 리스트가 비어있고 target 값이 0이 되면 1 반환
#         return 1
#     elif not numbers: #리스트가 비었는데 target이 0이 아니라면 0 반환
#         return 0
    
#     answer = solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0]) #
    
#     return answer
