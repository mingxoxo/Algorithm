# 로봇청소기
# 23.06.17
# https://www.acmicpc.net/problem/14503

def cleaning(x, y, d):
    global ans, room
    
    dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)

    if room[x][y] == '0':
        room[x][y] = '2'
        ans += 1
    
    for _ in range(4):
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]
        if room[nx][ny] == '0':
            return cleaning(nx, ny, d)
    
    nx, ny = x + dx[(d + 2) % 4], y + dy[(d + 2) % 4]
    
    if room[nx][ny] == '1':
        return -1

    return cleaning(nx, ny, d)



N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(input().split()) for _ in range(N)]
ans = 0
cleaning(r, c, abs(3 - d))
print(ans)

"""
# 풀이 2

def cleaning(x, y, d):
    global room
    dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)
    ans = 1

    while room[x][y] != '1':
        room[x][y] = '2'
       
        for _ in range(4):
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]
            if room[nx][ny] == '0':
                x, y = nx, ny
                ans += 1
                break
        else:
            x, y = x + dx[(d + 2) % 4], y + dy[(d + 2) % 4]
       
    return ans


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(input().split()) for _ in range(N)]
print(cleaning(r, c, abs(3 - d)))
"""
