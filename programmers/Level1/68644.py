#두 개 뽑아서 더하기
#https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    return sorted(list(set(answer)))
