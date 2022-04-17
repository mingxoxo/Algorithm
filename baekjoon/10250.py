#ACM 호텔
#https://www.acmicpc.net/problem/10250
#zfill함수 --> 숫자만큼 0을 왼쪽에 채워주는 함수

T = int(input())
for i in range(T):
    H, W, N = map(int, input().split()) #호텔 층수, 각 층의 방 수, 몇 번째 손님
    floor, ho = (N%H, N//H + 1) if N%H != 0 else (H, N//H)
    print(str(floor)+str(ho).zfill(2))

