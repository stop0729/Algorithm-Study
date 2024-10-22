# 게임 개발

N, M = map(int, input().split()) # 맵 크기 입력

d = [[0] * M for _ in range(N)] # 방문 처리하는 맵
x, y, direction = map(int, input().split()) # 현재 x, y, 방향 입력
d[x][y] = 1 # 현재 좌표 방문 처리

array = [] # 바다와 육지를 나타내는 원래 맵
for i in range(N): # 전체 맵 입력(1:바다, 0:육지)
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_count = 0 

# 방향 - 0:북, 1:동, 2:남, 3:서
#3->2->1->0->3->2->1->0
while True:
    # 왼쪽으로 회전
    direction -= 1
    if direction == -1:
        direction = 3
    turn_count += 1
    
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 후 가보지 않은 칸 & 육지
    if d[nx][ny] == 0 and array[nx][ny] == 0: 
        d[nx][ny] = 1 # 방문 처리
        x = nx
        y = ny
        count += 1
        turn_count = 0 # 이동하면 turn 횟수 초기화

    # 네 방향 모두 바다(1) & 방문(1) -> 한 칸 뒤
    # 북(0) <-> 남(2)
    # 동(1) <-> 서(3)
    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if array[nx][ny] == 1: # 바다이면
            break
        else:
            x = nx
            y = ny
            turn_count = 0 # 이동하면 turn 횟수 초기화
            d[nx][ny] = 1 # 방문 처리

print(count)        
        
        

