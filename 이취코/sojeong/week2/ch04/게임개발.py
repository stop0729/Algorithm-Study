# 게임 개발

N, M = map(int, input().split())

d = [[0] * M for _ in range(N)] # 맵 생성
x, y, direction = map(int, input().split()) # 현재 x, y, 방향 입력
d[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(N): # 전체 맵 입력
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    # 왼쪽으로 회전
    direction -= 1
    if direction == -1:
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 후 정면에 가보지 않은 칸이 존재하는 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        continue
    else:
        break
    

# 안 된건 왜 안됐는지 토론해보기