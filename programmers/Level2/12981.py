#영어 끝말잇기
#https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        if len(words[i]) == 1 or words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            answer[0] = i%n + 1
            answer[1] = i//n + 1
            break
            
    return answer
