#전화번호 목록
#효율성 3번, 4번 통과
#참고 : https://programmers.co.kr/questions/25120

def solution(phone_book):
    phone_book.sort(key = lambda x: (x, len(x)))
    for i in range(len(phone_book)-1):
        if phone_book[i+1].find(phone_book[i]) == 0:
            return False
    return True

#다른사람의 풀이
#startswith, 해쉬
