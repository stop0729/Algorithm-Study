# 블록 이동하기
# https://school.programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, board):
    N = len(board)
    q = deque([((x, y), (x, y + 1), 0)])  # 초기 상태, 이동 횟수 # ((x1, y1), (x2, y2), count)
    visited = set([((x, y), (x, y + 1))])  # 방문 표시 # {((0, 0), (0, 1))}
    print(visited)
    while q: # 큐가 빌 때까지
        (x1, y1), (x2, y2), count = q.popleft()

        # 종료 조건
        if (x1 == N - 1 and y1 == N - 1) or (x2 == N - 1 and y2 == N - 1): # (N-1, N-1)에 도달하면 종료
            return count

        # 네 방향 이동
        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]

            # 이동 가능 여부 확인
            if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0: # 벽(1)이 아닐 때
                    if ((nx1, ny1), (nx2, ny2)) not in visited: # 안 가본 곳이면
                        visited.add(((nx1, ny1), (nx2, ny2)))
                        q.append(((nx1, ny1), (nx2, ny2), count + 1))

        # 회전: 가로 방향에서 세로 방향으로
        if x1 == x2:  # 로봇이 가로로 있을 때
            for d in [-1, 1]:  # 위쪽 또는 아래쪽 회전
                if 0 <= x1 + d < N and board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0: # 위쪽이나 아래쪽이 다 벽이 아닐 때
                    # 로봇을 세로 방향으로 회전하여 추가
                    # 원래 : (0, 0),(0, 1) 이고, d=1이라면
                    if ((x1, y1), (x1 + d, y1)) not in visited:  # (0, 0),(1, 0)
                        visited.add(((x1, y1), (x1 + d, y1)))
                        q.append(((x1, y1), (x1 + d, y1), count + 1)) 
                    if ((x2, y2), (x2 + d, y2)) not in visited: # (0, 1),(1, 1)
                        visited.add(((x2, y2), (x2 + d, y2)))
                        q.append(((x2, y2), (x2 + d, y2), count + 1))

        # 회전: 세로 방향에서 가로 방향으로
        elif y1 == y2:  # 로봇이 세로로 있을 때
            for d in [-1, 1]:  # 왼쪽 또는 오른쪽 회전
                if 0 <= y1 + d < N and board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0: # 왼쪽이나 오른쪽이 다 벽이 아닐 때
                    # 로봇을 가로 방향으로 회전하여 추가
                    # 원래 : (0, 0), (1, 0) 이고, d=1이라면
                    if ((x1, y1), (x1, y1 + d)) not in visited: # (0, 0), (0, 1)
                        visited.add(((x1, y1), (x1, y1 + d)))
                        q.append(((x1, y1), (x1, y1 + d), count + 1))
                    if ((x2, y2), (x2, y2 + d)) not in visited: # (1, 0), (1, 1)
                        visited.add(((x2, y2), (x2, y2 + d)))
                        q.append(((x2, y2), (x2, y2 + d), count + 1))

    return -1  # 예외 

def solution(board):
    print(bfs(0, 0, board))
    #return bfs(0, 0, board)

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
# 7