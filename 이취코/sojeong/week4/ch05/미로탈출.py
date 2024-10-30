# 미로탈출
from collections import deque

N, M = map(int, input().split())
array = []
for i in range(N):
    array.append(list(map(int, input()))) # split : 공백 있을때만
    
# 위치:(1,1) , 출구:(N,M)
# 괴물 있는 부분 0, 없는 부분1 -> 1인 부분을 가야돼
# 움직여야 하는 최소 칸의 개수
dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)]) # (x, y) 튜플 형태로 넣기

    while queue: # 큐가 빌 때까지 
        x, y = queue.popleft() # 노드 꺼내기
        for i in range(4): # 4방향
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if array[nx][ny] == 1:
                    array[nx][ny] = array[x][y] + 1 # 최소 이동거리 수 계속 1씩 더함
                    queue.append((nx, ny))
    
    return array[N-1][M-1]

print(bfs(0,0))  # (0,0)에서 시작

'''
5 6
101010
111111
000001
111111
111111
'''


# 10