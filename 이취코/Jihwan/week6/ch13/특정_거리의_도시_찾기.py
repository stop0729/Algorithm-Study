from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque([X])

distance = [9999] * (N+1)
distance[X] = 0
    
def bfs(graph, start):
    while queue:
        start = queue.popleft()
        cost = distance[start]
        for i in graph[start]:
            if cost + 1 < distance[i]:
                distance[i] = cost + 1
                queue.append(i)

bfs(graph, X)

print(distance)
toggle = 0
for i in range(len(distance)):
    if distance[i] == K:
        toggle = 1
        print(i)

if toggle == 0:
    print(-1)