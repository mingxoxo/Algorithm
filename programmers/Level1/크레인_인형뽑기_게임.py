#https://programmers.co.kr/learn/courses/30/lessons/64061
#2중 for문으로 푸시는 분도 있었음
#cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))

def solution(board, moves):
    answer = 0

    N = len(board)
    board_T = [list(x) for x in zip(*board)]
    doll = [board_T[i].count(0) for i in range(N)]
    basket = []

    for i in moves:
        if doll[i-1] >= N:
            continue

        if basket[-1:] == [board_T[i-1][doll[i-1]]]:
            answer += 2
            basket.pop()
        else:
            basket.append(board_T[i-1][doll[i-1]])
        doll[i-1] += 1

    return answer
