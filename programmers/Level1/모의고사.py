def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_list = []

    person_list = list([person1, person2, person3])
    for person in person_list: #for q, a in enumerate(answers): 을 사용해서 한번에 index도 받아올 수 있음
        count = 0
        for i in range(len(answers)):
            if person[i%len(person)] == answers[i]:
                count+=1
        count_list.append(count)
    for i in range(3): #[i + 1 for i, v in enumerate(s) if v == max(s)]로 줄일 수 있음 !!!
        if count_list[i] == max(count_list):
            answer.append(i+1)
    
    return sorted(answer)
