#전화번호 목록
#효율성 3번, 4번 시간초과

#1
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[j]) < len(phone_book[i]):
                break
            if phone_book[j].find(phone_book[i]) == 0:
                return False
    return True
 

#2
def solution(phone_book):
    phone_book.sort(key = len)
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].find(phone_book[i]) == 0:
                return False
    return True
