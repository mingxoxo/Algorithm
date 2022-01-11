#키패드 누르기
#https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    finger = {'L' : (3, 0), 'R' : (3, 2)}
    location = [(3, 1), (0, 0), (0, 1), (0, 2),(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
        elif n in [3, 6, 9]:
            answer += 'R'
        else:
            l = sum([abs(finger['L'][i] - location[n][i]) for i in range(2)])
            r = sum([abs(finger['R'][i] - location[n][i]) for i in range(2)])
            if l == r:
                answer += hand[0].upper()
            elif l < r:
                answer += 'L'
            else :
                answer += 'R'
                
        finger[answer[-1]] = location[n]
            
    
    return answer
