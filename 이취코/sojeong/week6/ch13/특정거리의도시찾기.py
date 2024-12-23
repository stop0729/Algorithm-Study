# https://www.acmicpc.net/problem/18352

from collections import deque

# 입력
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# BFS를 이용한 최단 거리 계산
def bfs(start):
    # 거리 정보를 저장하는 리스트 (-1로 초기화)
    distance = [-1] * (N + 1)
    distance[start] = 0  # 시작 도시의 거리는 0
    
    # BFS 탐색
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1:  # 아직 방문하지 않은 도시
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    
    return distance

# 거리 계산
distances = bfs(X)

# 거리 K인 도시 찾기
result = [i for i in range(1, N + 1) if distances[i] == K]

# 결과 출력
if result:
    print("\n".join(map(str, sorted(result))))
else:
    print(-1)
