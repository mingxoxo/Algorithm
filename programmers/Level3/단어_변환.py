https://programmers.co.kr/learn/courses/30/lessons/43163#
# 각각 떼서 합집합이 len + 1일 때 겹친다고 볼 수 있다. --> set을 이용하면 중복된 변수가 사라지기 때문에 구현 불가 
# 따라서 np.array로 변환 후 == 값을 통해 값 비교 / np.equal()함수를 썼을 때 오류 발생
# BFS
import numpy as np

def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    visited = [0 for i in range(len(words))]

    queue = [begin]
    while queue:
        length = len(queue)
        for k in range(length):
            search = queue.pop(0)
            for i in range(len(words)):
                a = np.array(list(search))
                b = np.array(list(words[i]))
                if list(a == b).count(False) == 1:
                    queue.append(words[i])
                    visited[i] = 1
                # if visited[i] == 0 and (len(set(search) & set(words[i])) == len(set(target)) - 1):
        answer += 1
        if target in queue:
            return answer
    return 0


# begin = "hit"
# target = "hhh"
# words = ["hhh", "hht"]
#
# print(solution(begin, target, words))

#제너레이터를 사용하는 방법이 있었음

