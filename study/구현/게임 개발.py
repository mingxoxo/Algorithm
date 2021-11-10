# 게임 개발
# N * M 크기의 직사각형 / 각각의 칸은 육지 또는 바다 / 캐릭터는 동서남북 중 한 곳을 바라봄
# 맵의 각 칸 (A, B) / A:  북쪽으로부터 떨어진 칸 개수, B: 서쪽으로부터 멀어진 칸의 개수
# 바다로 되어있는 공간은 갈 수 없다.

# 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def visited_map(game_map, x, y, direction, visited, cnt):
    count = 0
    while True:
        while count < 4:
            print(x, y, direction)
            count += 1
            direction = (direction + 3) % 4  # 왼쪽 방향
            dx = move[direction][0]
            dy = move[direction][1]
            try:
                if visited[x + dx][y + dy] is False:  # 왼쪽방향 안가봤으면
                    visited[x + dx][y + dy] = True
                    cnt += 1
                    x = x + dx
                    y = y + dy
                    count = 0
            except:
                continue
        try:
            if visited[x - dx][y - dy] is True:
                if game_map[x - dx][y - dy] == 1:
                    break
                else:
                    x = x - dx
                    y = y - dy
                    count = 0
        except:
            break
    return cnt


N, M = map(int, input().split())
print(N, M)
firstX, firstY, direction = map(int, input().split())
print(firstX, firstY, direction)
cnt = 1

game_map = []
visited = []
for i in range(N):
    game_map.append(list(map(int, input().split())))
    visited.append([bool(int(x)) for x in game_map[i]])  # 외우자

visited[firstX][firstY] = True
print(visited_map(game_map, firstX, firstY, direction, visited, cnt))
