#https://programmers.co.kr/learn/courses/30/lessons/42584
#초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
#가격이 떨어지지 않은 기간은 몇 초인지를 return

def solution(prices):
    answer = [0] * len(prices)
    stack_price = [(0, prices[0])]
    for i in range(1, len(prices)):
        while stack_price and stack_price[-1][1] > prices[i]:
            lower = stack_price.pop()
            answer[lower[0]] = i - lower[0]
        stack_price.append((i, prices[i]))
    while stack_price:
        lower = stack_price.pop()
        answer[lower[0]] = len(prices) - 1 - lower[0]
        
    return answer
