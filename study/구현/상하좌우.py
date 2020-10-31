N = int(input()) #공간의 크기
plan = input().split() #계획서 내용
x ,y = 1, 1

for direction in plan:
  if(direction == 'L' and y != 1):
    y-=1;
  elif(direction == 'R' and y != N):
    y+=1;
  elif(direction == 'U' and x != 1):
    x-=1;
  elif(direction == 'D' and x != N):
    x+=1;

print(x, y) #최종적으로 도착할 지점의 좌표


# 답안 예시
#dx = [0, 0, -1, 1] dy = [-1, 1, 0, 0] move_types = ['L', 'R', 'U', 'D']
# 위의 리스트를 사용하여 for문을 작성
