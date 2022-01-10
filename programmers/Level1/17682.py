#[1차] 다트 게임
#https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    score = []
    area = {'S' : 1, 'D' : 2, 'T' : 3}
    s = ''
    
    for i in dartResult:
        if i.isdigit():
            s += i
        elif i == '*':
            if len(score) >= 2:
                score[-2] *= 2
            score[-1] *= 2
        elif i == '#':
            score[-1] *= -1
        elif i in area.keys():
            score.append(int(s)**area[i])
            s = ''

    return sum(score)
