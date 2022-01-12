#큰 수 만들기 (테스트케이스 10번 시간초과)
#https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ""
    num_list = list(number)
    for i in range(len(number)-k, 0, -1):
        l = len(num_list)
        if i == l:
            answer += ''.join(num_list)
            break
        answer += max(num_list[:l-i+1])
        num_list = num_list[num_list.index(answer[-1])+1:]
    
    return answer
