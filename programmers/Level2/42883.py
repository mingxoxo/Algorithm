#큰 수 만들기
#https://programmers.co.kr/learn/courses/30/lessons/42883

#stack으로 코드 구현 - 테스트케이스 10번 시간초과 해결
#참고 - https://programmers.co.kr/questions/12094

def solution(number, k):
    answer = []
    num_list = list(number)
    cnt = 0
    for i in range(len(number)):
        while answer and answer[-1] < num_list[i]:
            answer.pop()
            cnt += 1
            if cnt == k:
                answer += num_list[i:]
                return ''.join(answer)
        answer.append(num_list[i])
    
    return ''.join(answer[:-k]) #같은 수가 계속 반복되면 삭제가 되지 않게됨
